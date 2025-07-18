#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    // Define the color to be used for replacing black pixels
    RGBTRIPLE color;        // Pau-brasil wood color
    color.rgbtRed = 172;    // Set the intensity of red
    color.rgbtGreen = 0;    // Set the intensity of green
    color.rgbtBlue = 47;    // Set the intensity of blue

    // Iterate over each pixel in the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Check if the current pixel is black
            if (image[i][j].rgbtRed == 0 && image[i][j].rgbtGreen == 0 && image[i][j].rgbtBlue == 0)
            {
                // Replace the black pixel with the chosen color
                image[i][j] = color;
            }
        }
    }
}
