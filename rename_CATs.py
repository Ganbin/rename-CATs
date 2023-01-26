import json
import subprocess

# Test
# To get the tails.json file : https://api.taildatabase.com/enterprise/tails
# Need to add "x-api-version: 2" header
# More info: https://api.taildatabase.com/docs/#/TAIL%20Database%20Enterprise%20API%20v2.0%20(Beta)/TailController_getTailsV2

file = open("tails.json")
data = json.load(file)
alias = "/Applications/Chia.app/Contents/Resources/app.asar.unpacked/daemon/chia"
fingerprint = "3564051972"

# chia wallet show -f 0123456789 | grep "Asset ID"
myCats = [
    "a628c1c2c6fcb74d53746157e438e108eab5c0bb3e5c80ff9b1910b3e4832913",
    "8f27f8b6aa31e07f4de43e12eea854ab450d56afdd65be4328928f5bd2fa80cb",
    "d2039f75557be47a2679bd870949d834c943208e2a33cc798fc8bb6d6b95af48",
    "f7d33a036caf9a111a68213d3f2307b67f09f016d8b132e37df96d250d716df4",
    "287b633167f822353444492c96030db71ee78e6ac33897ea4c572623aa4c94d2",
    "2ed236fe3fa979eaad87d89d10f9156539526f8b6c60d6f341f9de5b1f7c19f5",
    "482b49902d310c53065c3531d398d41808f1390590d566815d67040f6a32d124",
    "8ebf855de6eb146db5602f0456d2f0cbe750d57f821b6f91a8592ee9f1d4cf31",
    "bd960d5a150ed1b4f2242fc5761097b017b530d19dc2943f5e1907a6be1a0d09",
    "a82b3a2d2b9bb4d9fbdb4bd3bfce4bf56a1d1859a366e56fecf95790aed49094",
    "94621bf6d74f26866812a69b9bc7cb2b25507b9f5717ebd768c1ec0ac63796aa",
    "e5a8af7124c2737283838e6797b0f0a5293fc81aca1ffd2720f8506c23f2ad88",
    "b3867458a6af107794a09b6083e3f0f05fbece0adae328f4df9ade53a60ca1b3",
    "7108b478ac51f79b6ebf8ce40fa695e6eb6bef654a657d2694f1183deb78cc02",
    "4e34fb4247865a1a644c992a51340aa32f397f094cf1abd9663803ed4e172dfc",
    "8a0208f53687ca9dfc5ea48dd14396461707848baeae6230b4977b05654ea8a0",
    "6651a352a4b9c0973faedf5f2e03ca187a0306b8402487d12c505b48881eeb97",
    "5fd27391e6385e5d4bdc5b7b2df67b2e8698e337d49b94302a3551deda565e58",
    "49fd76384a4fced922d99d28a646dd0439ab753ad15fcfea8ef50213804112e6",
    "0f8676bd61b83d8cc8543cf75a54bb6963ea7c9465eb2da4b84901778ad37d3f",
    "22945c6c10f2c1be9f4b2484652768498cf1e4153c015a7bf981913a6b21430a",
    "5de2b461a7257e1451bf1c331cbfc55945c39e02b2e540f05e596963c410003d",
    "ea3e045df9fe9a7844cbb56f500bd146354d9e6f8c970b2ff8f8842d77442e97",
    "0ed71c399419b16df76ae7cde9fa257f1dbf845bef462b7f9ea6de8d181cdf97",
    "79f6313fdb6ba66347a5bcad4af6878ac07bf5fafedeb384c3b350d913c8b6b6",
    "ec25b77bc54df637392d6a0f542de65f45020405d0f36ced723bff2870c378b1",
    "86290de455ae081dfe44c099743cb8eae18c705f461922280d138c24ac8c3110",
    "824c71e37ac660006e03f7884561e7a124d930460ae1506a9c234c06ebc6aa1d",
    "98be421bf2afd03bbaa71d7217216837790a9ea7a710f0b684cc9a4cc9f6f153",
    "b8edcc6a7cf3738a3806fdbadb1bbcfc2540ec37f6732ab3a6a4bbcd2dbec105",
    "fe65842a8b4f20c212360e22ad3da51d3b30020b29fd0a7b395ae60fcc6f6321",
    "d92268a1df8aa91aa410fcfaaa57583562bdfe9bacb458453f3518c4a3256124",
    "5a1ddb8379d9547e68a71e870103f9a5cfb049dbf83eec309e4df9e166a01b98",
    "db1a9020d48d9d4ad22631b66ab4b9ebd3637ef7758ad38881348c5d24c38f20",
    "6d3d2c9709d8e89d4707fa4f5f3e69269bd0b825a22da4fa45ed517da95136e0",
    "948b43068a09895cdfdf3a3eae857eec450a34677fe69fc5ce39df36b3a40fec",
    "4c4380af7d15c896d9e6266f322ac494c398803032eef56f2ab65877956d007f",
    "14b40962dfef81d954ac0d92b51ec21ce7acd8c62dd9fef9303aa51c615cb495",
    "69776ba48bada66d8be4a4dd97290e73197fe20f1cfb294429be5304bd3527ed",
    "1dadf5b097d2e1257d375759aaa15298ed3e0f70b6de275d9c70dc2f7eca14a8",
    "319ad6d73f87f62f446765b03c55af860e2c3dcac9105a78532038f4056a9160",
    "4ec438355a6b7506cb85e7d330e758d7b30d0bcf44021517f094ed878f74afe0",
]

for tail in data["tails"]:
    if ("code" in tail) and ("name" in tail) & (tail["hash"] in myCats):
        name = tail["code"] + " - " + tail["name"]
        subprocess.call(
            [
                alias,
                "wallet",
                "add_token",
                "-f",
                fingerprint,
                "-id",
                tail["hash"],
                "-n",
                name,
            ]
        )

file.close()
