#!/usr/bin/env python3
user_input = input("Please enter an IPv4 IP address:")

## the line below creates a single string that is passed to print()
# print("You told me the IPv4 address is:" + user_input)

## print() can be given a series of objects separated by a comma
print("You told me the IPv4 address is:", user_input)

vender_input = input("Please enter vender name: ")

print("You have a", vender_input, "with an IPV4 address of", user_input)

print(f"You have a {vendor_input} with an IPV4 address of {user_input}.")
