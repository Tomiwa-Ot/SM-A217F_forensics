### Extract dialer codes from device
```bash
package_name_trim=$(pm list packages -s -f | awk -F 'package:' '{print $2}' | awk -F '=' '{print $2}')

for i in ${package_name_trim}; do
  echo "${i}" && pm dump "${i}" | grep -E 'Scheme: "android_secret_code"|Authority: "[0-9].*"|Authority: "[A-Z].*"' >> extracted_codes.txt
done
```
