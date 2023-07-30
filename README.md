# Dynamic DNS Updater for Godaddy

#### What is this and how it works?

> This is a very simple script meant to be used as a cronjob to update 'A' records using the [Godaddy API](https://developer.godaddy.com/doc/endpoint/domains#/v1/recordGet). This should be useful as a starting point to automate DNS automations.

To get started, first check the [official documentation](https://developer.godaddy.com/getstarted) and read carefully how to retrive an API key.


#### Command:
```sh
./updater -k <key> -s <secret> -d <domain> -h <host>

```
