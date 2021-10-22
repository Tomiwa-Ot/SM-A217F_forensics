## USB Switcher
Expose modem interface via USB

### Dependency
libusb
- Linux: install libusb via your package manager
- Windows: https://github.com/pyusb/pyusb/blob/master/docs/faq.rst#how-do-i-install-libusb-on-windows

### Setup
```console
user@vm:~$ pip install requirements.txt
user@vm:~$ python3 usbswitcher.py -h
usage: usbswitcher [-h] [--idVendor IDVENDOR] [--idProduct IDPRODUCT]

Description: switches USB configuration
[+] Default idVendor: 0x04e8 (Samsung)
[+] Default idProduct: 0x6860 (Samsung)

optional arguments:
  -h, --help            show this help message and exit
  --idVendor IDVENDOR   Vendor ID of the device <class 'int'>
  --idProduct IDPRODUCT
                        Product ID of the device <class 'int'>
```

### 
- No Backend Available: https://github.com/pyusb/pyusb/blob/master/docs/faq.rst#how-do-i-fix-no-backend-available-errors
- Resource Busy: ¯\\\_(ツ)_/¯