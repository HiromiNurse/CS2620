import numpy as np


def gaussian_kernel(size, fuzzyness):
    kernel = np.fromfunction(
        lambda x, y: (1/(2 * np.pi * fuzzyness ** 2)) *
        np.exp( -((x - (size - 1) / 2) ** 2 + (y - (size - 1) / 2) ** 2) / (2 * fuzzyness ** 2)
        ), (size, size)
    )
    return kernel / np.sum(kernel)


def applyKernel(image, kernel):
    image_array = np.array(image)

    pad_size = len(kernel) // 2
    padded_image = np.pad(image_array, ((pad_size, pad_size), (pad_size, pad_size), (0, 0)), mode='edge')

    height, width = image_array.shape[:2]

    output_image = np.zeros(image_array.shape)

    for i in range(height):
        for j in range(width):
            for k in range(3):
                output_image[i, j, k] = np.sum(kernel * padded_image[i:i + len(kernel), j:j + len(kernel), k])

    output_image = np.clip(output_image, 0, 255)

    return output_image.astype(np.uint8)

def applyKernelNoPadding(image, kernel):
    image_array = np.array(image)
    kernel_size = len(kernel)
    kernel_radius = kernel_size // 2

    height, width = image_array.shape[:2]

    output_image = np.zeros((height - 2 * kernel_radius, width - 2 * kernel_radius, 3))

    for y in range(kernel_radius, height - kernel_radius):
        for x in range(kernel_radius, width - kernel_radius):
            for z in range(3):
                output_image[y - kernel_radius, x - kernel_radius, z] = np.sum(
                    kernel * image_array[y - kernel_radius:y + kernel_radius + 1,
                             x - kernel_radius:x + kernel_radius + 1, z]
                )

    output_image = np.clip(output_image, 0, 255)

    return output_image.astype(np.uint8)


def kernelShenanigan():
    kernels = {
        "edge": [
            [0, -1, 0],
            [-1, 4, -1],
            [0, -1, 0]
        ],
        "goon": [
            [-1, -1, -1],
            [-1, 8, -1],
            [-1, -1, -1]
        ],
        "unsharp": [
            [1 * -(1/256), 4 * -(1/256), 6 * -(1/256), 4 * -(1/256), 1 * -(1/256)],
            [4 * -(1/256), 16 * -(1/256), 24 * -(1/256), 16 * -(1/256), 4 * -(1/256)],
            [6 * -(1/256), 24 * -(1/256), -476 * -(1/256), 24 * -(1/256), 6 * -(1/256)],
            [4 * -(1/256), 16 * -(1/256), 24 * -(1/256), 16 * -(1/256), 4 * -(1/256)],
            [1 * -(1/256), 4 * -(1/256), 6 * -(1/256), 4 * -(1/256), 1 * -(1/256)]
        ], # multiply by -1/256
        "sharpen": [
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ]
    }
    keys = list(kernels.keys())
    count = 0
    for key in kernels:
        print(f"{count:5}: {key:20}")
        count += 1
    select = int(input("Select the number corresponding to the kernel you want to use: "))
    if 0 <= select < len(keys):
        return kernels[keys[select]]
    else:
        print("Invalid Selection")
        return None
