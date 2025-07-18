#include <math.h>    // for round function
#include <stdlib.h>  // for calloc and free functions
#include <stdio.h>   // for printf function
#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE pixel = image[i][j];
            // Calculate average of RGB values
            BYTE average = round((pixel.rgbtRed + pixel.rgbtGreen + pixel.rgbtBlue) / 3.0);

            // Assign the average value to each RGB component
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average; 
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE pixel = image[i][j];

            // Apply sepia formula to each RGB component
            int sepiaRed = round(0.393 * pixel.rgbtRed + 0.769 * pixel.rgbtGreen + 0.189 * pixel.rgbtBlue);
            int sepiaGreen = round(0.349 * pixel.rgbtRed + 0.686 * pixel.rgbtGreen + 0.168 * pixel.rgbtBlue);
            int sepiaBlue = round(0.272 * pixel.rgbtRed + 0.534 * pixel.rgbtGreen + 0.131 * pixel.rgbtBlue);

            // Cap the values at 255 if they exceed by ternary operator
            image[i][j].rgbtRed = (sepiaRed > 255) ? 255 : sepiaRed;
            image[i][j].rgbtGreen = (sepiaGreen > 255) ? 255 : sepiaGreen;
            image[i][j].rgbtBlue = (sepiaBlue > 255) ? 255 : sepiaBlue;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // Swap pixels from left and right sides
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a temporary copy of the image
    RGBTRIPLE(*tempImage)[width] = calloc(height, width * sizeof(RGBTRIPLE));
    if (tempImage == NULL)
    {
        printf("Not enough memory to store temporary image.\n");
        return;
    }

    // Iterate over each pixel in the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int count = 0;
            int redSum = 0;
            int greenSum = 0;
            int blueSum = 0;

            // Iterate over each neighboring pixel (including the current pixel itself)
            for (int k = -1; k <= 1; k++)
            {
                for (int l = -1; l <= 1; l++)
                {
                    int row = i + k;
                    int col = j + l;

                    // Check if the neighboring pixel is within the image bounds
                    if (row >= 0 && row < height && col >= 0 && col < width)
                    {
                        // Accumulate the RGB values of neighboring pixels
                        redSum += image[row][col].rgbtRed;
                        greenSum += image[row][col].rgbtGreen;
                        blueSum += image[row][col].rgbtBlue;
                        count++;
                    }
                }
            }

            // Calculate the average RGB values and assign them to the current pixel in the temporary image
            tempImage[i][j].rgbtRed = round((float)redSum / count);
            tempImage[i][j].rgbtGreen = round((float)greenSum / count);
            tempImage[i][j].rgbtBlue = round((float)blueSum / count);
        }
    }

    // Copy the blurred pixels back to the original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = tempImage[i][j];
        }
    }

    // Free the memory allocated for the temporary image
    free(tempImage);
}