# NS Firewall Testing Script

Python script used to test the firewalls we setup for
Canes Pte Ltd for our Network Security module in
Ngee Ann Polytechnic, Year 2 Semester 1.

## Overview of Features

- Testing of Web Traffic (allow Google, block Taobao)
- Testing of Email Traffic (allow SMTP)
- Testing of Remote Access Traffic (allow SSH & RDP)
- General implementation that can be used to test both KL & SG
- VPN Connectivity Testing

---

## Testing Notes

1. An `openssl.cnf` file must be created with the following contents:

```txt
openssl_conf = default_conf

[ default_conf ]

ssl_conf = ssl_sect

[ssl_sect]

system_default = ssl_default_sect

[ssl_default_sect]

Options = UnsafeLegacyRenegotiation
```

2. Set the `OPENSSL_CONF` environment variable to the path of the `openssl.cnf` file.
