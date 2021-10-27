## SM-A217F (carrier unlocked) AT Commands
Enable 3GPP in developer options

> However, it was discovered that an attacker can still access the modem by switching to a secondary USB configuration even when both USB tethering and USB debugging (i.e. ADB) are disabled and when the device is locked. Samsung devices exposes MTP as USB configuration 1 and CDC ACM modem (for AT commands) as USB Configuration 2 (regardless of whether USB debugging is enabled or disabled). Thus, the attacker has to switch the device USB configuration to the CDC ACM modem (i.e. USB configuration 2) using [usbswitcher](usbswitcher/).

USB Descriptors: https://beyondlogic.org/usbnutshell/usb5.shtml
```console
user@vm:~$ lsusb -v
...
Bus 001 Device 007: ID 04e8:6860 Samsung Electronics Co., Ltd Galaxy (MTP)
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               2.00
  bDeviceClass            0 
  bDeviceSubClass         0 
  bDeviceProtocol         0 
  bMaxPacketSize0        64
  idVendor           0x04e8 Samsung Electronics Co., Ltd
  idProduct          0x6860 Galaxy series, misc. (MTP mode)
  bcdDevice            4.19
  iManufacturer           1 SAMSUNG
  iProduct                2 SAMSUNG_Android
  iSerial                 3 RF8N72DAHDP
  bNumConfigurations      2
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength       0x002f
    bNumInterfaces          1
    bConfigurationValue     1
    iConfiguration          4 Conf 1
    bmAttributes         0x80
      (Bus Powered)
    MaxPower              500mA
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           3
      bInterfaceClass         6 Imaging
      bInterfaceSubClass      1 Still Image Capture
      bInterfaceProtocol      1 Picture Transfer Protocol (PIMA 15470)
      iInterface              5 MTP
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x81  EP 1 IN
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0200  1x 512 bytes
        bInterval               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x01  EP 1 OUT
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0200  1x 512 bytes
        bInterval               1
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x82  EP 2 IN
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x001c  1x 28 bytes
        bInterval               6
        INTERFACE CLASS:  08 24 80 0c 00 01 00 01
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength       0x0071
    bNumInterfaces          3
    bConfigurationValue     2
    iConfiguration          4 Conf 1
    bmAttributes         0x80
      (Bus Powered)
    MaxPower              500mA
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           3
      bInterfaceClass         6 Imaging
      bInterfaceSubClass      1 Still Image Capture
      bInterfaceProtocol      1 Picture Transfer Protocol (PIMA 15470)
      iInterface              5 MTP
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x81  EP 1 IN
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0200  1x 512 bytes
        bInterval               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x01  EP 1 OUT
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0200  1x 512 bytes
        bInterval               1
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x82  EP 2 IN
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x001c  1x 28 bytes
        bInterval               6
        INTERFACE CLASS:  08 24 80 0c 00 01 00 01
    Interface Association:
      bLength                 8
      bDescriptorType        11
      bFirstInterface         1
      bInterfaceCount         2
      bFunctionClass          2 Communications
      bFunctionSubClass       2 Abstract (modem)
      bFunctionProtocol       1 AT-commands (v.25ter)
      iFunction               8 CDC Serial
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        1
      bAlternateSetting       0
      bNumEndpoints           1
      bInterfaceClass         2 Communications
      bInterfaceSubClass      2 Abstract (modem)
      bInterfaceProtocol      1 AT-commands (v.25ter)
      iInterface              6 CDC Abstract Control Model (ACM)
      CDC Header:
        bcdCDC               1.10
      CDC Call Management:
        bmCapabilities       0x00
        bDataInterface          2
      CDC ACM:
        bmCapabilities       0x02
          line coding and serial state
      CDC Union:
        bMasterInterface        1
        bSlaveInterface         2 
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x84  EP 4 IN
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x000a  1x 10 bytes
        bInterval               9
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        2
      bAlternateSetting       0
      bNumEndpoints           2
      bInterfaceClass        10 CDC Data
      bInterfaceSubClass      0 
      bInterfaceProtocol      0 
      iInterface              7 CDC ACM Data
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x83  EP 3 IN
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0200  1x 512 bytes
        bInterval               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x02  EP 2 OUT
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0200  1x 512 bytes
        bInterval               0
Device Qualifier (for other device speed):
  bLength                10
  bDescriptorType         6
  bcdUSB               2.00
  bDeviceClass            0 
  bDeviceSubClass         0 
  bDeviceProtocol         0 
  bMaxPacketSize0        64
  bNumConfigurations      2
Device Status:     0x0000
  (Bus Powered)
```

> As a result of previous work (CVE-2016-4030, CVE-2016-4031, and CVE-2016-4032), Samsung has locked down the exposed AT interface with a command whitelist.
> This whitelist is active when the ro.product_ship property is set to true and limits the commands to information gathering only. Any non-whitelisted command responds with the generic reply of OK, even if it is invalid.

Certain AT commands may not work. Changing the ro.product_ship property in ```/system/build.prop``` to False may deactivate the whitelist. To do this, the device should either be rooted or have a custom ROM installed.

## Requirements
- pyserial

## CheatSheet
- List Ports
```console
user@pc:~$ python -m serial.tools.list_ports -v
```

- Access Port
```console
user@pc:~$ python -m serial.tools.miniterm <port_name>
```

### The following are AT commands extracted from Samsung [A217FXXU5BUB4/A217FOJM5BUB6](https://www.getgsmtips.com/samsung-galaxy-a21s-sm-a217f-u5-full-firmware/) firmware

- [AP (Application Processor or PDA) AT Commands](at%20commands/AP.md)

- [CP (Core Processor/Modem) AT Commands](at%20commands/CP.md)

### NB
- Other common [AT Commands](at%20commands/others.md)
- List supported commands: [AT+CLAC](at%20commands/AT+CLAC.md)