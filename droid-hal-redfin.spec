# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device redfin
%define vendor google

%define vendor_pretty Google
%define device_pretty Pixel 5

%define installable_zip 1

%define makefstab_skip_entries /product /system /system_ext /vendor

%define straggler_files \
/bugreports\
/cache\
/d\
/sdcard\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

