{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5bea042e-f10c-45a8-b4ef-f2148705a24d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "import time\n",
    "import numpy as np\n",
    "from plyer import notification"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d4cc985-0209-46ad-88c1-7ff6f25aea8e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load IDS model\n",
    "with open ('C:/Users/Admin/Desktop/Ids_model' , 'rb') as file:\n",
    "    model = pickle.load(file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3c51f7a-f958-4740-b480-fec09ffe83f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Feature extraction\n",
    "def live_features():\n",
    "    features = {'Flow Duration': 123456.0,\n",
    "        'Total Fwd Packets': 50,\n",
    "        'Total Backward Packets': 48,\n",
    "        'Flow Bytes/s': 65234.5,\n",
    "        'Flow IAT Mean': 2345.6,\n",
    "        'Packet Length Mean': 600.4,\n",
    "        'Packet Length Std': 34.6,\n",
    "        'Fwd Packet Length Mean': 300.2,\n",
    "        'Init Win Bytes Forward': 1024,\n",
    "        'PSH Flag Count': 1,\n",
    "        'ACK Flag Count': 1}\n",
    "    \n",
    "    input_array = np.array([[features[col] for col in ['Flow Duration', 'Total Fwd Packets', 'Total Backward Packets',\n",
    "        'Flow Bytes/s', 'Flow IAT Mean', 'Packet Length Mean',\n",
    "        'Packet Length Std', 'Fwd Packet Length Mean', 'Init Win Bytes Forward',\n",
    "        'PSH Flag Count', 'ACK Flag Count']]])\n",
    "    \n",
    "    return input_array \n",
    "\n",
    "def check_intrusion(): # check + prediction\n",
    "    features = live_features()\n",
    "    prediction = model.predict(features)\n",
    "    \n",
    "    if prediction[0] == 1: # 1 --> Ddos (Abnormal)\n",
    "        notification.notify(\n",
    "            title = 'IDS Alert',\n",
    "            message = 'System under possible cyber attack!',  \n",
    "            timeout = 5\n",
    "        )\n",
    "        print(\"[ALERT] Attack Detected!\")\n",
    "\n",
    "# Runs in background to check the intrusion\n",
    "while True:\n",
    "    check_intrusion()\n",
    "    time.sleep(20) #cheack for every 20 sec"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6063ffd5-9307-4838-8080-c3c3e9d85150",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
