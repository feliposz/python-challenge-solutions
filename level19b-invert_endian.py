import array,wave
wi = wave.open('indian.wav','rb')
wo = wave.open('indian_inv.wav', 'wb')
wo.setparams(wi.getparams())
a = array.array('i')
a.fromstring(wi.readframes(wi.getnframes()))
a.byteswap()
wo.writeframes(a.tostring())
wi.close(),wo.close()
