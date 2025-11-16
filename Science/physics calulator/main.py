from tkinter import *
from functions import *  # Import physics calculation functions from external file

class Ui():
    def __init__(self, root):
        self.root = root
        self.root.title("Physics Calculator")

        # Create frames for each section
        self.ohms_frame = Frame(self.root, background='Grey')
        self.wavesframe = Frame(self.root, background='Grey')
        self.snells_frame = Frame(self.root, background='Grey')

        # Initialize widgets and layout
        self.creater_widgets()
        self.display_widgets()

    # -------------------- OHM'S LAW --------------------
    def submit_ohms_button(self):
        # Get input values
        voltage = self.ohms_entries['voltage_entry'].get()
        current = self.ohms_entries['current_entry'].get()
        resistance = self.ohms_entries['resistance_entry'].get()

        # Determine which field is empty and calculate it
        try:
            if voltage == '':
                result = ohms_law('voltage', current=float(current), resistance=float(resistance))
                self.ohms_entries['voltage_entry'].delete(0, END)
                self.ohms_entries['voltage_entry'].insert(0, str(round(result, 2)))
            elif current == '':
                result = ohms_law('current', voltage=float(voltage), resistance=float(resistance))
                self.ohms_entries['current_entry'].delete(0, END)
                self.ohms_entries['current_entry'].insert(0, str(round(result, 2)))
            elif resistance == '':
                result = ohms_law('resistance', voltage=float(voltage), current=float(current))
                self.ohms_entries['resistance_entry'].delete(0, END)
                self.ohms_entries['resistance_entry'].insert(0, str(round(result, 2)))
        except Exception as e:
            print("Error:", e)

    def clear_ohms_entries(self):
        # Clear all Ohm's Law entry fields
        for entry in self.ohms_entries.values():
            entry.delete(0, END)

    # -------------------- WAVES --------------------
    def submit_waves_button(self):
        # Get input values
        wave_speed = self.waves_entries['wavespeed_entry'].get()
        frequency = self.waves_entries['frequency_entry'].get()
        wavelength = self.waves_entries['wavelength_entry'].get()

        # Determine which field is empty and calculate it
        try:
            if wave_speed == '':
                result = waves_func('wave speed', lambda_=float(wavelength), frequency=float(frequency))
                self.waves_entries['wavespeed_entry'].delete(0, END)
                self.waves_entries['wavespeed_entry'].insert(0, str(round(result, 2)))
            elif frequency == '':
                result = waves_func('frequency', wave_speed=float(wave_speed), lambda_=float(wavelength))
                self.waves_entries['frequency_entry'].delete(0, END)
                self.waves_entries['frequency_entry'].insert(0, str(round(result, 2)))
            elif wavelength == '':
                result = waves_func('wavelength', wave_speed=float(wave_speed), frequency=float(frequency))
                self.waves_entries['wavelength_entry'].delete(0, END)
                self.waves_entries['wavelength_entry'].insert(0, str(round(result, 2)))
        except Exception as e:
            print("Error:", e)

    def clear_waves_entries(self):
        # Clear all wave entry fields
        for entry in self.waves_entries.values():
            entry.delete(0, END)

    # -------------------- SNELL'S LAW --------------------
    def submit_snells_button(self):
        # Get input values
        n1 = self.snells_entries['n1_entry'].get()
        theta1 = self.snells_entries['theta1_entry'].get()
        n2 = self.snells_entries['n2_entry'].get()
        theta2 = self.snells_entries['theta2_entry'].get()

        # Determine which refractive index is missing and calculate it
        try:
            if n1 == '':
                result = refractiveindex_law('n1', n2=float(n2), theta1=float(theta1), theta2=float(theta2))
                self.snells_entries['n1_entry'].delete(0, END)
                self.snells_entries['n1_entry'].insert(0, str(round(result, 3)))
            elif n2 == '':
                result = refractiveindex_law('n2', n1=float(n1), theta1=float(theta1), theta2=float(theta2))
                self.snells_entries['n2_entry'].delete(0, END)
                self.snells_entries['n2_entry'].insert(0, str(round(result, 3)))
        except Exception as e:
            print("Error:", e)

    def clear_snells_entries(self):
        # Clear all Snell's Law entry fields
        for entry in self.snells_entries.values():
            entry.delete(0, END)

    # -------------------- WIDGET CREATION --------------------
    def creater_widgets(self):
        # Ohm's Law widgets
        self.ohms_labels = {
            'voltage_label': Label(self.ohms_frame, text='Voltage (V)', bg='grey', fg='Light Blue'),
            'current_label': Label(self.ohms_frame, text='Current (A)', bg='grey', fg='Light Blue'),
            'resistance_label': Label(self.ohms_frame, text='Resistance (Ω)', bg='grey', fg='Light Blue')
        }
        self.ohms_entries = {
            'voltage_entry': Entry(self.ohms_frame, bg='Light Grey'),
            'current_entry': Entry(self.ohms_frame, bg='Light Grey'),
            'resistance_entry': Entry(self.ohms_frame, bg='Light Grey')
        }

        # Wave widgets
        self.waves_labels = {
            'wavespeed_label': Label(self.wavesframe, text='Wave Speed (m/s)', bg='grey', fg='Light Blue'),
            'frequency_label': Label(self.wavesframe, text='Frequency (Hz)', bg='grey', fg='Light Blue'),
            'wavelength_label': Label(self.wavesframe, text='Wavelength (m)', bg='grey', fg='Light Blue')
        }
        self.waves_entries = {
            'wavespeed_entry': Entry(self.wavesframe, bg='Light Grey'),
            'frequency_entry': Entry(self.wavesframe, bg='Light Grey'),
            'wavelength_entry': Entry(self.wavesframe, bg='Light Grey')
        }

        # Snell's Law widgets
        self.snells_labels = {
            'n1_label': Label(self.snells_frame, text='n₁ (Refractive Index)', bg='grey', fg='Light Blue'),
            'theta1_label': Label(self.snells_frame, text='θ₁ (degrees)', bg='grey', fg='Light Blue'),
            'n2_label': Label(self.snells_frame, text='n₂ (Refractive Index)', bg='grey', fg='Light Blue'),
            'theta2_label': Label(self.snells_frame, text='θ₂ (degrees)', bg='grey', fg='Light Blue')
        }
        self.snells_entries = {
            'n1_entry': Entry(self.snells_frame, bg='Light Grey'),
            'theta1_entry': Entry(self.snells_frame, bg='Light Grey'),
            'n2_entry': Entry(self.snells_frame, bg='Light Grey'),
            'theta2_entry': Entry(self.snells_frame, bg='Light Grey')
        }

        # Buttons for all sections
        self.buttons = {
            'ohms_submit': Button(self.ohms_frame, text='Submit', command=self.submit_ohms_button),
            'ohms_clear': Button(self.ohms_frame, text='Clear', command=self.clear_ohms_entries),
            'waves_submit': Button(self.wavesframe, text='Submit', command=self.submit_waves_button),
            'waves_clear': Button(self.wavesframe, text='Clear', command=self.clear_waves_entries),
            'snells_submit': Button(self.snells_frame, text='Submit', command=self.submit_snells_button),
            'snells_clear': Button(self.snells_frame, text='Clear', command=self.clear_snells_entries)
        }

    # -------------------- LAYOUT DISPLAY --------------------
    def display_widgets(self):
        # Ohm's Law layout
        self.ohms_frame.pack(padx=10, pady=10, fill=X)
        for i, key in enumerate(self.ohms_labels):
            self.ohms_labels[key].grid(row=i, column=0, padx=5, pady=5)
        for i, key in enumerate(self.ohms_entries):
            self.ohms_entries[key].grid(row=i, column=1, padx=5, pady=5)
        self.buttons['ohms_submit'].grid(row=3, column=0, pady=10)
        self.buttons['ohms_clear'].grid(row=3, column=1, pady=10)

        # Waves layout
        self.wavesframe.pack(padx=10, pady=10, fill=X)
        for i, key in enumerate(self.waves_labels):
            self.waves_labels[key].grid(row=i, column=0, padx=5, pady=5)
        for i, key in enumerate(self.waves_entries):
            self.waves_entries[key].grid(row=i, column=1, padx=5, pady=5)
        self.buttons
        
        # Snells law layout
        self.snells_frame.pack(padx=10, pady=10, fill=X)
        for i, key in enumerate(self.snells_labels):
            self.snells_labels[key].grid(row=i, column=0, padx=5, pady=5)
        for i, key in enumerate(self.snells_entries):
            self.snells_entries[key].grid(row=i, column=1, padx=5, pady=5)
        self.buttons['snells_submit'].grid(row=4, column=0, pady=10)
        self.buttons['snells_clear'].grid(row=4, column=1, pady=10)


if __name__ == '__main__':
    master = Tk()
    master.config(background='Grey')
    run = Ui(master)
    master.mainloop()