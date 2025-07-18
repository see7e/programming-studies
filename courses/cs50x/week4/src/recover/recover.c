#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// Definitions
#define FILENAME_SIZE 8
#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Open forensic image file
    FILE *raw_file = fopen(argv[1], "r");
    if (raw_file == NULL)
    {
        printf("Could not open %s as reading file.\n", argv[1]);
        return 1;
    }

    // Variables
    int file_count = 0;
    FILE *outfile = NULL;
    uint8_t buffer[BLOCK_SIZE];
    char filename[FILENAME_SIZE];

    while (fread(buffer, sizeof(uint8_t), BLOCK_SIZE, raw_file) == BLOCK_SIZE)
    {
        // Check for JPEG header
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close previous file (if any)
            if (outfile != NULL)
            {
                fclose(outfile);
                outfile = NULL;
            }

            // Create new JPEG file
            snprintf(filename, FILENAME_SIZE, "%03i.jpg", file_count);
            outfile = fopen(filename, "w");
            if (outfile == NULL)
            {
                printf("Could not create %s.\n", filename);
                fclose(raw_file);
                return 1;
            }
            file_count++;
        }

        // Write to JPEG file (if open)
        if (outfile != NULL)
        {
            fwrite(buffer, sizeof(uint8_t), BLOCK_SIZE, outfile);
        }
    }

    // Close files
    if (outfile != NULL)
    {
        fclose(outfile);
    }
    fclose(raw_file);
    return 0;
}