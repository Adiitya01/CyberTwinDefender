from pydantic import BaseModel
from typing import List

class IDSInput(BaseModel):
    Flow_Duration: float
    Total_Fwd_Packets: float
    Total_Backward_Packets: float
    Flow_Bytes_s: float
    Flow_IAT_Mean: float
    Packet_Length_Mean: float
    Packet_Length_Std: float
    Fwd_Packet_Length_Mean: float
    Init_Win_Bytes_Forward: float
    PSH_Flag_Count: int
    ACK_Flag_Count: int

class EmailInput(BaseModel):
    text:str