import numpy as np
import matplotlib.pyplot as plt


def sin_waveform(input_data, frequency=50):
    return np.sin(2 * np.pi * frequency * input_data)


def downsampler_to_20_hz(input_data=None):
    result = np.array([])
    for index in np.arange(0, 50, 5):
        result = np.append(result, input_data[index])
        result = np.append(result, (input_data[index + 2] + input_data[index + 3]) * 0.5)
    return result


if __name__ == "__main__":
    x = np.linspace(0, 1, 50, endpoint=False)
    print(x)
    upsample_from_5_hz = sin_waveform(input_data=x,
                                      frequency=5)
    upsample_from_20_hz = sin_waveform(input_data=x,
                                       frequency=20)
    # plt.plot(x,
    #          upsample_from_20_hz,
    #          "r")
    # plt.plot(x,
    #          upsample_from_20_hz,
    #          "rs")

    downsample_to_20_hz = downsampler_to_20_hz(input_data=upsample_from_20_hz)

    plt.plot(np.linspace(0, 1, 20, endpoint=False),
             sin_waveform(input_data=np.linspace(0, 1, 20, endpoint=False),
                          frequency=20))

    plt.plot(np.linspace(0, 1, 20, endpoint=False),
             downsample_to_20_hz,
             "go")
    plt.show()
