pip install opencv-python
pip install pyzbar
pip install numpy
pip install ipython
pip install uvcorn
pip install fastapi
pip install qrcode[pil] - Tool to generate QR code


qr "Some text" > test.png

##

To run the appln
----------------
uvicorn main:app --reload
http://127.0.0.1:8000/docs

To run from ipython
-------------------
import blockchain
bc = blockchain.Blockchain()
bc.chain
bc.mine_block("Apple iPhone 11-MHCX3LL/A")
bc.min_block("Sony OLED TV 55 Inch")
bc.chain
bc.min_block("LG washing Machine")
bc.is_chain_valid()
bc.chain[1]["Sony OLED TV 55 Inch"]="Sanyo OLED TV 55 Inch"
bc.is_chain_valid()