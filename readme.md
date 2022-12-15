# Renaming CATs
This little script if very basic and help to rename all the CATs in the wallet.

This is usefull when resetting the wallet for example. Or if we buy a lot of new CATs :).

## Manual steps needed
There is some manual steps that may be done before this script to work.

### 1. Get JSON of all the TAILs
There is a tails.json file that contain all the tails informations.

To renew the tails.json file : https://api.taildatabase.com/enterprise/tails
Need to add "x-api-version: 2" header
More info: https://api.taildatabase.com/docs/#/TAIL%20Database%20Enterprise%20API%20v2.0%20(Beta)/TailController_getTailsV2

### 2. Get the list of you CATs asset IDs from your wallet
I use `chia wallet show -f 0123456789 | grep "Asset ID"` to get the list of asset ID. I then format it like that:

```python
["a628c1c2c6fcb74d53746157e438e108eab5c0bb3e5c80ff9b1910b3e4832913",...,...]
```
(Don't forget to replace the `-f` by your own fingerprint.)

Replace the `myCats` variable in the `rename_CATs.py` file.

### 3. You can now run the script and Voila!