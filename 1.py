{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "nilai anda: 50\n",
      "nilai anda bukan: 60\n",
      "====================================================================================================\n",
      "nilai anda adalah C\n",
      "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n",
      "operator logika untuk list dan string\n",
      " \n",
      "\"saya gak jual sepatu \"\n",
      "tidak ada z di sepatu\n"
     ]
    }
   ],
   "source": [
    "nilai = 50\n",
    "\n",
    "if nilai != 75:\n",
    "    print(\"nilai anda:\",nilai)\n",
    "\n",
    "if nilai is 60: # equal\n",
    "    print(\"nilai anda:\")\n",
    "\n",
    "if nilai is not 60: # not equal\n",
    "    print(\"nilai anda bukan: 60\")\n",
    "\n",
    "print(100*\"=\")\n",
    "\n",
    "nilai = 65\n",
    "\n",
    "if 80 < nilai < 100:\n",
    "    print(\"nilai anda adalah A\")\n",
    "elif 70 < nilai < 80:\n",
    "    print(\"nilai anda adalah B\")\n",
    "elif 60 < nilai < 70:\n",
    "    print(\"nilai anda adalah C\")\n",
    "elif 50 < nilai < 60:\n",
    "    print(\"nilai anda adalah T, lakukan perbaikan\")\n",
    "else:\n",
    "    print(\"maaf anda tidak lulus mata kuliah ini\")\n",
    "\n",
    "print(100*\"+\")\n",
    "print(\"operator logika untuk list dan string\")\n",
    "print(\" \")\n",
    "\n",
    "gorengan=[\"bakwan\",\"cireng\",\"bala-bala\",\"gehu\",\"combro\",\"pisang goreng\",\"pukis\",\"risoles\"]\n",
    "beli = \"sepatu\"\n",
    "\n",
    "if beli in gorengan:\n",
    "    print('Mamang bilang, \" ya, saya jual',beli,'\"')\n",
    "\n",
    "if not beli in gorengan:\n",
    "    print('\"saya gak jual',beli,'\"')\n",
    "\n",
    "karakter = \"z\"\n",
    "if karakter in beli:\n",
    "    print(\"ada\", karakter, \"di\",beli)\n",
    "else:\n",
    "    print(\"tidak ada\",karakter,\"di\",beli)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
