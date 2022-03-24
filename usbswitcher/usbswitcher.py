#!/usr/bin/env python3

'''
usbswitcher.py by @Tomiwa-Ot

Search for an attached USB Samsung device and switch it to a specific USB
configuration. Requires libusb

References:
[1] https://github.com/pyusb/pyusb
'''


import argparse
import sys
import usb.core

vendor_id = 0x04e8	# Samsung Vendor ID
product_id = 0x6860	# Samsung Product ID
CONFIGURATION_VALUES = []


def parse_args():
	global vendor_id, product_id
	parser = argparse.ArgumentParser(
		prog="usbswitcher",
		description="Description: switches USB configuration\n" \
			"[+] Default idVendor: 0x04e8 (Samsung)\n" \
			"[+] Default idProduct: 0x6860 (Samsung)",
		formatter_class=argparse.RawTextHelpFormatter
	)
	parser.add_argument(
		"--idVendor", type=int, required=False,
		help="Vendor ID of the device <class 'int'>"
	)
	parser.add_argument(
		"--idProduct", type=int, required=False,
		help="Product ID of the device <class 'int'>"
	)
	args = parser.parse_args()
	if args.idVendor is not None:
		vendor_id = args.idVendor
	if args.idProduct is not None:
		product_id = args.idProduct


def main():
	parse_args()
	try:
		dev = usb.core.find(idVendor=vendor_id, idProduct=product_id)
		if dev is None:
			sys.stderr.write("[+] Device Not Found\n")
			sys.exit(1)
		sys.stdout.write(
			"[+] Number of configurations found: {}\n"
			.format(dev.bNumConfigurations)
		)
		for cfg in dev:
			CONFIGURATION_VALUES.append(cfg.bConfigurationValue)
		sys.stdout.write(
			"[+] Available configurations: {}\n" \
			"[+] Active configuration: {}\n"
			.format(
				str(CONFIGURATION_VALUES),
				dev.get_active_configuration().bConfigurationValue
			)
		)
		if dev.get_active_configuration().bConfigurationValue == CONFIGURATION_VALUES[0]:
			dev.set_configuration(CONFIGURATION_VALUES[1])
			sys.stdout.write(
				"[+] Configuration switched to {}\n"
				.format(dev.get_active_configuration().bConfigurationValue)
			)
		else:
			dev.set_configuration(CONFIGURATION_VALUES[0])
			sys.stdout.write(
				"[+] Configuration switched to {}\n"
				.format(dev.get_active_configuration().bConfigurationValue)
			)
	except usb.core.NoBackendError as error:
		sys.stderr.write("{}\n".format(str(error)))
	except usb.core.USBError as error:
		sys.stderr.write("{}\n".format(str(error)))
	except NotImplementedError as error:
		sys.stderr.write("{}\n".format(str(error)))


if __name__ == "__main__":
	sys.exit(main())
