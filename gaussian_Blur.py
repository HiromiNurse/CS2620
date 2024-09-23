import numpy as np


def gaussian_kernel(size, fuzzyness):
    kernel = np.fromfunction(
        lambda x, y: (1/(2 * np.pi * fuzzyness ** 2)) * np.exp(
             -((x - (size - 1) / 2) ** 2 + (y - (size - 1) / 2) ** 2) / (2 * fuzzyness ** 2)
        ), (size, size)
    )
    return kernel / np.sum(kernel)


def applyKernel(image, kernel):
    image_array = np.array(image)

    pad_size = len(kernel) // 2
    padded_image = np.pad(image_array, ((pad_size, pad_size), (pad_size, pad_size), (0, 0)), mode='edge')
    image_array = np.array(image_array)

    height, width = image_array.shape[:2]

    output_image = np.zeros(image_array.shape)

    for i in range(height):
        for j in range(width):
            for k in range(3):
                output_image[i, j, k] = np.sum(kernel * padded_image[i : i + len(kernel), j : j + len(kernel), k])

    output_image = np.clip(output_image, 0, 255)

    return output_image.astype(np.uint8)

def applyKernelNoPadding(image, kernel):
    kernel_size = len(kernel)
    kernel_radius = kernel_size // 2
    image_array = np.array(image)

    height, width = image_array.shape[:2]

    output_image = np.zeros(image_array.shape)

    print(image_array)

    for i in range(kernel_radius, height - kernel_radius):
        for j in range(kernel_radius, width - kernel_radius):
            for k in range(3):
                output_image[i - kernel_radius, j - kernel_radius, k] = np.sum(kernel * image_array[i-kernel_radius:i + kernel_radius+1, j-kernel_radius:j+kernel_radius+1, k])

    output_image = np.clip(output_image, 0, 255)

    return output_image.astype(np.uint8)
