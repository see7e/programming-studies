---
title: Old Dell Latitude XT
tags:
  - linux
  - old
  - pc
  - dell
  - latitude_xt
  - programming
use: Blog
languages: 
dependences:
---

# Installing Linux on an old PC

I've always been kind with using old hardware, the feeling of the old movies where the hacker is using a old computer to hack the mainframe is probably where the desire of being a programmer started.

But life is a interesting thing, it brings mostly want you think that you don't want, but is mostly what you need. So my path taked some turns but now I've ended up with a old (pretty new) Dell Latitude XT, a tablet PC from 2007.

It already had Windows 10 Pro installed but I didn't wanted another MS machine, so this is how I installed Linux on it, what I've faced and how I solved it.


## Trying Arch btw

The firsts steps were smoth, following some random tutorial, but in some point of the isntalation (the exact point doesn't matters now, you'll see) the same error was bein raised, tried to troubleshoot for some hours but I wasn't getting any progress, so I decided tto swap the OS with some lightweight linux distro and ended up with a 32bit XFCE MX version, that was really pleasnt to configure.

## The Configuration

To connect to the network internet, just used the `nmcli` if you don't have `net-tools availabletool with `nmcli device wifi list` that returns the list of available 

Installed the distro by the normal process, and starting as they say: ricing. The first step was to clean and remove most of the Desktop apps and elements that could consume the little (to none) memory available. After that changed the behaviour and other aspects of the theme, to more details lookup at the [xfce-desktop-configuration](../../Projects/.dotfiles/docs/xfce4.md).

## Upgrading

As you might expect with all the epic spec that the Latitude has (a 1.33GHz Intel Core 2 Duo and 3Mb of DDR2 RAM) this machine is as fast as an old turtle. So what to improve? You may ask. After doiung some research I found three different possibilities:

- upgrading the memory, the easiest, after all the DDR2-800 PC2-6400 isn't this rare, and the prices aren't too high;
- upgrading the storage, and here we find more problems because the connection of the drive is made with an zif cable, and after some time spent looking for an adapter I've managed to find this [one](https://pt.aliexpress.com/item/32886601850.html?gatewayAdapt=glo2bra). At leats is something right?
- upgrading the processor, and this is the most problematic possibility beacuse involve removing a pletora of screws and almost every piece only to reach the motherboard.

Taking in consideration the topics above I'll be looking forward to achieve at least the first two.bye.
