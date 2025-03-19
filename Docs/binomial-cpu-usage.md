---
title: Corretalation between Binomiial Distribution and CPU Usage - Algorithm
tags: studies, programming
use: Documentation, Algorithms
languages: C
dependences: math.h, stdio.h, stdlib.h, string.h, dirent.h
---

# Prof of concept

Stumbled accros this function when reading Tanembaum's [Modern Operating Systems](https://www.amazon.com/Modern-Operating-Systems-Andrew-Tanenbaum/dp/013359162X) and wanted to test out the function creating a program to retrieve the information and calculate the value describled in the section 2.1.7 Modeling the Multiprogramming.

The formula $CPU Usage = 1 - p^n$, where `p` is the fraction of time the CPU is idle and `n` is the number of processes in the system. So the program retrieves the system's CPU and RAM information, counts the number of running processes, and computes CPU usage.

Researching about the topic I found this [article](https://en.wikipedia.org/wiki/Binomial_distribution) that explains the binomial distribution and how it can be used to model the probability of a given number of successes in a fixed number of trials.

I found interesting that the formula, presented above looks like a simplification of the binomial distribution formula, where `p` is the probability of success and `n` is the number of trials.

Rather the similarity between the two formulas, the CPU usage formula takes a more deterministic approach, assuming that the CPU is either idle or busy, and the number of processes is fixed. In contrast, the binomial distribution considers the probability of success in each trial and allows for a range of possible outcomes.

The CPU usage formula although simplified, assumes idle time behavior in a way that mirrors, but does not replicate, the assumptions underlying the binomial distribution.

## Overview of the Program

> [!NOTE]
> This C program is designed for Linux systems, relying on the `/proc` filesystem to gather system information. It provides an educational example of how to access system-level details using C.

The program performs the following steps:

1. **Get CPU Information**: Reads the number of CPU cores and the CPU frequency.
2. **Get RAM Information**: Retrieves the total RAM available.
3. **List Running Processes**: Counts the number of running processes.
4. **Compute CPU Usage**: Calculates the CPU usage based on idle time and the number of processes.

## Code Breakdown

### Include Required Headers

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <math.h>
```

- **`stdio.h`**: Standard input/output library for functions like `printf` and `fgets`.
- **`stdlib.h`**: Standard library for functions like `malloc`, `free`, and `exit`.
- **`string.h`**: Provides string manipulation functions like `strncmp` and `sscanf`.
- **`dirent.h`**: Used for directory handling, specifically to read the `/proc` directory.
- **`math.h`**: Provides mathematical functions, particularly `pow` for calculating powers.

### Get CPU Information

```c
void get_cpu_info(int *cpu_count, double *cpu_freq) {
    FILE *cpuinfo = fopen("/proc/cpuinfo", "r");
    char buffer[BUFFER_SIZE];
    *cpu_count = 0;
    *cpu_freq = 0.0;

    while (fgets(buffer, BUFFER_SIZE, cpuinfo)) {
        if (strncmp(buffer, "processor", 9) == 0) {
            (*cpu_count)++;
        }
        if (strncmp(buffer, "cpu MHz", 7) == 0) {
            sscanf(buffer, "cpu MHz : %lf", cpu_freq);
        }
    }
    fclose(cpuinfo);
}
```

- **`fopen("/proc/cpuinfo", "r")`**: Opens the `/proc/cpuinfo` file for reading. This file contains detailed information about the CPU.
- **`fgets(buffer, BUFFER_SIZE, cpuinfo)`**: Reads each line of the file.
- **`strncmp(buffer, "processor", 9)`**: Checks if the line starts with "processor", indicating a CPU core. The count is incremented each time, giving the total number of CPU cores.
- **`sscanf(buffer, "cpu MHz : %lf", cpu_freq)`**: Parses the CPU frequency (in MHz) from the line starting with "cpu MHz".
- **`fclose(cpuinfo)`**: Closes the file after reading.

### Get RAM Information

```c
double get_ram_info() {
    FILE *meminfo = fopen("/proc/meminfo", "r");
    char buffer[BUFFER_SIZE];
    double total_memory = 0.0;

    while (fgets(buffer, BUFFER_SIZE, meminfo)) {
        if (strncmp(buffer, "MemTotal", 8) == 0) {
            sscanf(buffer, "MemTotal: %lf kB", &total_memory);
            total_memory /= 1024 * 1024;  // Convert kB to GB
            break;
        }
    }
    fclose(meminfo);
    return total_memory;
}
```

- **`fopen("/proc/meminfo", "r")`**: Opens the `/proc/meminfo` file for reading. This file provides memory usage information.
- **`fgets(buffer, BUFFER_SIZE, meminfo)`**: Reads each line of the file.
- **`strncmp(buffer, "MemTotal", 8)`**: Checks if the line starts with "MemTotal", which indicates the total memory available.
- **`sscanf(buffer, "MemTotal: %lf kB", &total_memory)`**: Parses the total memory in kilobytes and converts it to gigabytes.
- **`fclose(meminfo)`**: Closes the file after reading.

### List Running Processes

```c
int get_running_processes() {
    struct dirent *entry;
    DIR *dp = opendir("/proc");
    int process_count = 0;

    if (dp == NULL) {
        perror("opendir");
        return -1;
    }

    while ((entry = readdir(dp)) != NULL) {
        if (entry->d_type == DT_DIR && isdigit(entry->d_name[0])) {
            process_count++;
        }
    }
    closedir(dp);
    return process_count;
}
```

- **`opendir("/proc")`**: Opens the `/proc` directory, which contains information about running processes and system information.
- **`readdir(dp)`**: Reads each directory entry in `/proc`.
- **`entry->d_type == DT_DIR && isdigit(entry->d_name[0])`**: Checks if the entry is a directory and its name starts with a digit, which would indicate a process ID (PID) directory.
- **`process_count++`**: Increments the count for each valid process directory found.
- **`closedir(dp)`**: Closes the `/proc` directory after reading.

### Get CPU Idle Time

```c
double get_idle_time() {
    FILE *statfile = fopen("/proc/stat", "r");
    char buffer[BUFFER_SIZE];
    double idle_time = 0.0;
    
    if (fgets(buffer, BUFFER_SIZE, statfile)) {
        char cpu_label[5];
        unsigned long long int user, nice, system, idle;
        sscanf(buffer, "%s %llu %llu %llu %llu", cpu_label, &user, &nice, &system, &idle);
        idle_time = (double) idle / (user + nice + system + idle);
    }
    fclose(statfile);
    return idle_time;
}
```

- **`fopen("/proc/stat", "r")`**: Opens the `/proc/stat` file, which contains various statistics about the system, including CPU usage.
- **`fgets(buffer, BUFFER_SIZE, statfile)`**: Reads the first line of the file, which contains aggregate CPU statistics.
- **`sscanf(buffer, "%s %llu %llu %llu %llu", cpu_label, &user, &nice, &system, &idle)`**: Extracts the CPU times for different states: `user`, `nice`, `system`, and `idle`.
- **`idle_time = (double) idle / (user + nice + system + idle)`**: Calculates the proportion of time the CPU was idle.
- **`fclose(statfile)`**: Closes the file after reading.

### Calculate CPU Usage

```c
double calculate_cpu_usage(double idle_time, int running_processes) {
    return 1.0 - pow(idle_time, running_processes);
}
```

- **`pow(idle_time, running_processes)`**: Raises the idle time proportion to the power of the number of running processes.
- **`1.0 - ...`**: Subtracts the result from 1.0 to calculate the CPU usage based on the formula provided.

### Main Function

```c
int main() {
    int cpu_count;
    double cpu_freq;
    double total_memory;
    int running_processes;
    double idle_time, cpu_usage;

    get_cpu_info(&cpu_count, &cpu_freq);
    total_memory = get_ram_info();
    running_processes = get_running_processes();
    idle_time = get_idle_time();
    cpu_usage = calculate_cpu_usage(idle_time, running_processes);

    // Print system information
    printf("CPU Count: %d\n", cpu_count);
    printf("CPU Frequency: %.2f MHz\n", cpu_freq);
    printf("Total RAM: %.2f GB\n", total_memory);

    // Print running processes count
    printf("Running Processes: %d\n", running_processes);

    // Print calculated CPU usage
    printf("Calculated CPU Usage: %.2f%%\n", cpu_usage * 100);

    return 0;
}
```

- **Variable Declarations**: Declares variables to hold CPU count, CPU frequency, total memory, number of running processes, idle time, and CPU usage.
- **Function Calls**: Calls the previously defined functions to populate the variables with system information.
- **`printf` Statements**: Prints the retrieved system information and calculated CPU usage.
- **`return 0`**: Indicates successful program execution.


---

The formula $1 - p^n$ and the binomial distribution both involve concepts of probability and repeated independent trials. However, they serve different purposes and are used in different contexts.

While there are parallels in their structure, the CPU usage formula is a deterministic approximation rather than a true probability distribution, a more general and widely applicable statistical model.