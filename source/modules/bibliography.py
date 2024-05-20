#!/usr/bin/python3

def credit_me():
    with open('source/version.txt', 'r') as file:
        version_number = file.readline().strip()
    print(f"Version {version_number} of G2N2")
    print("Written by Lukas Blacklock. Email issues to ljb1crt@bolton.ac.uk or create an issue at https://github.com/lukasjab/G2N2/issues")