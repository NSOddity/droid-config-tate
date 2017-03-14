# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc

%define device tate
%define vendor amazon

%define vendor_pretty Amazon
%define device_pretty Kindle Fire HD 7

%define dcd_path ./

# adjust this for your device
%define pixel_ratio 1.5

# We assume most devices will
%define have_modem 0

%include droid-configs-device/droid-configs.inc
