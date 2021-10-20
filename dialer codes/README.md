### Extract dialer codes from device
```bash
package_name_trim=$(pm list packages -s -f | awk -F 'package:' '{print $2}' | awk -F '=' '{print $2}')

for i in ${package_name_trim}; do
  echo "${i}" && pm dump "${i}" | grep -E 'Scheme: "android_secret_code"|Authority: "[0-9].*"|Authority: "[A-Z].*"' >> extracted_codes.txt
done
```

<table>
  <tr>
    <td align="center" width="20%">
      <img src="screenshots/USB_settings.jpg"><br>
      <span><b>*#0808#</b></span> 
    </td>
    <td align="center" width="20%">
      <img src="screenshots/version.jpg"><br>
      <span><b>*#1234#</b></span> 
    </td>
  </tr>
  <tr>
    <td align="center" width="20%">
      <img src="screenshots/battery_status.jpg"><br>
      <span><b>*#0228#</b></span> 
    </td>
    <td align="center" width="20%">
      <img src="screenshots/camera_light_sensor.jpg"><br>
      <span><b>*#8727#</b></span>
    </td>
  </tr>
  <tr>
    <td align="center" width="20%">
      <img src="screenshots/receive_call_mode.jpg"><br>
      <span><b>*#7277#</b></span> 
    </td>
    <td align="center" width="20%">
      <img width="50%" src="screenshots/sysdump1.jpg"><img width="50%" src="screenshots/sysdump2.jpg"><img  width="50%" src="screenshots/sysdump3.jpg"><br>
      <span><b>*#9900#</b></span>
    </td>
  </tr>
   <tr>
    <td align="center" width="20%">
      <img src="screenshots/hw_module_test.jpg"><br>
      <span><b>*#0*#</b></span> 
    </td>
    <td align="center" width="20%">
      <img src="screenshots/service_mode9090.jpg"><br>
      <span><b>*#9090#</b></span>
    </td>
  </tr>
  <tr>
    <td align="center" width="20%">
      <img src="screenshots/service_mode1111.jpg"><br>
      <span><b>*#1111#</b></span> 
    </td>
    <td align="center" width="20%">
      <img src="screenshots/service_mode2222.jpg"><br>
      <span><b>*#2222#</b></span>
    </td>
  </tr>
  <tr>
    <td align="center" width="20%">
      <img src="screenshots/service_mode0011.jpg"><br>
      <span><b>*#0011#</b></span> 
    </td>
    <td align="center" width="20%">
      <img src="screenshots/cp_debug_level.jpg"><br>
      <span><b>*#66336#</b></span>
    </td>
  </tr>
  <tr>
    <td align="center" width="20%">
      <img width="50%" src="screenshots/device_keystring1.jpg"><img width="50%" src="screenshots/device_keystring2.jpg"><br>
      <span><b>*#2663#</b></span> 
    </td>
    <td align="center" width="20%">
      <img src="screenshots/samplemanagement.jpg"><br>
      <span><b>*#7676#</b></span>
    </td>
  </tr>
  </tr>
    <tr>
    <td align="center" width="20%">
      <img src="screenshots/imei_sn.jpg"><br>
      <span><b>*#06#</b></span> 
    </td>
    <td align="center" width="20%">
      <img src="screenshots/device_keystring3.jpg"><br>
      <span><b>*#7785#</b></span>
    </td>
  </tr>
</table>
