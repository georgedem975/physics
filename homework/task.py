import builtins
import numpy as np
import matplotlib.pyplot as plt


def getSpectra(delta_t, lambda_0, time_values_of_the_pulse):
    return np.sinc(time_values_of_the_pulse / delta_t) * np.exp(
        2 * np.pi * lambda_0 * time_values_of_the_pulse * -1j)


def getIntervalLen(range_spectra):
    interval = np.argwhere(range_spectra >= np.max(range_spectra) / 2)
    return interval[-1] - interval[0]


def calculate_width(range_spectra):
    print_width = (((getIntervalLen(range_spectra) / (builtins.len(pulse) * delta_t))
                    / (2 * np.sqrt(2 * np.log(2))) * lambda_0 ** 2) * 1e+9)[0]

    builtins.print("Спектральная ширина пакета = ", print_width, "нм")


def calculate_fwhm(indixes):
    return (np.max(np.where(indixes)[0]) - np.min(np.where(indixes)[0])) * spectra_freq_delta


def plot_pulse():
    plt.plot(time_values_of_the_pulse, np.abs(pulse), color="b")
    plt.grid()
    plt.ylabel("Амплитуда")
    plt.xlabel("Время (сек)")
    plt.title("Изначальный импульс")
    plt.show()
    for b_i in [1, 10, 100]:
        new_spectra = spectra * np.exp(2 * np.pi * np.sqrt(3e8 ** 2
                                                           + (
                                                                       b_i ** 2 * frequencies_in_the_spectrum ** 2)) * time_values_of_the_pulse * -1j)
        new_pulse = np.abs(np.fft.ifftshift(np.fft.ifft(new_spectra)))
        old_pulse = np.abs(pulse)
        print("Характерное время расплывания пакета для b", b_i, "= ",
              calculate_fwhm(np.abs(np.fft.fftshift(np.fft.ifftshift(np.fft.ifft(new_spectra)))) < np.max(np.abs(np.fft.fftshift(np.fft.ifftshift(np.fft.ifft(new_spectra))))) / 2), "c")
        plt.plot(time_values_of_the_pulse, new_pulse, label=f"Искаженный", color="r", linewidth=3)
        plt.plot(time_values_of_the_pulse, old_pulse, label="Первоначальный", color="b")
        plt.ylabel("Амплитуда")
        plt.xlabel("Время (сек)")
        plt.title(f"b={b_i}")
        plt.legend()
        plt.grid()
        plt.show()
    new_spectra = spectra * np.exp(2 * np.pi * np.sqrt(3e8 ** 2
                                                       + (
                                                                   1 ** 2 * frequencies_in_the_spectrum ** 2)) * time_values_of_the_pulse * -1j)
    new_pulse = np.fft.ifftshift(np.fft.ifft(new_spectra))

    tmp = calculate_fwhm(np.abs(np.fft.fftshift(new_pulse) < np.max(np.abs(np.fft.fftshift(new_pulse))) / 2))

    tmp = np.linspace(0, tmp , 1024)  # возьмем время расплывания пакета
    plt.ylabel("Амплитуда")
    plt.xlabel("Время (сек)")
    plt.plot(tmp, abs(np.convolve(cod_of_message, new_pulse)[:1024]), color="b", linewidth=3)
    plt.title(f"Закодированное сообщение {message}")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    message="Zinchik"
    delta_t = 10e-6
    lambda_0 = 1.5e-6
    time_values_of_the_pulse = np.arange(-45 * delta_t, 45 * delta_t, 0.5 * delta_t)
    spectra = getSpectra(delta_t, lambda_0, time_values_of_the_pulse)
    spectra_freq_delta = abs(spectra[1] - spectra[2])
    pulse = np.fft.ifftshift(np.fft.ifft(spectra))
    frequencies_in_the_spectrum = np.fft.fftfreq(len(pulse), d=delta_t)
    calculate_width((np.abs(np.fft.fft(pulse))))
    code_of_message = np.zeros(1024)
    for i, letter in enumerate(message):
        code_of_message[128 * i] = ord(letter)
    plot_pulse()
