# Pwdgen
Just a simple password generator written in python3.9.   
This program lets you choose between different charsets which can be combined to create a password.   

<br>

## Requirementes
The only thing needed is to have python3 or above installed.   

<br>

## Usage
This program contains a shebang for Linux users which doesn't matter for Windows users so:
* For Linux and MacOSx users:
  ```bash
  ./pwdgen [flags] [password length]
  ```
  &nbsp;   
* For Windows users:
  ```cmd
  python pwdgen [flags] [password length]
  ```   
  Multiple [flags](#flags) can be specified specified to include different charset combinations for the password.   
  A password length may also be specified. If the password length is not specified, it'll default to 8.   
  The same goes to the flags: if no flags are specified, it'll default to all, so just running the raw program without arguments would result in a strong, 8 characters long password that uses upper and lower chars, numbers and symbols, resulting in a quick-access strong password.
  
<br>

## Flags
At least <b> one </b> of the following is required:   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-h, --help       show this help message and exit   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-u, --upper      adds uppercase characters to the password generation   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-l, --lower      adds lower characters to the password generation   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-n, --numbers    adds numbers to the password generation   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-s, --symbols    adds symbols to the password generation   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-m, --alnum      uses alphanumerical characters for the password generation   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-a, --all        uses all available sets for the password   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-S, --strong     same as -a, --all. Just an alias   
