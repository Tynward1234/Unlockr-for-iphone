bplist00�
X$versionY$archiverT$topX$objects ��_NSKeyedArchiver�	Troot��+1259=>CGKU$null�_attributedStringData]dataPersisterV$class����WNS.dataO�import sys
import usbmuxd
import time
import tqdm

def unlock_iphone(udid):
# Connect to the iPhone via usbmuxd
client = usbmuxd.Client()
iphone = None


for i in range(10):
try:
iphone = client.get_device(udid)
break
except usbmuxd.MuxError as e:
time.sleep(1)

if iphone is None:
print("Failed to connect to iPhone.")
return

try:
with tqdm.auto.trange(100) as pbar:
for i in range(100):
iphone.send_message("lockdown", "do_set_passcode", {
"passcodeEnabled": False
})
pbar.update(1)
time.sleep(1)
except usbmuxd.MuxError as e:
print(f"Failed to unlock the iPhone: {e}")

client.release(iphone)

udid = "your-udid-here"
unlock_iphone(udid)*(**(*	*(**(**(**(*V*(**(**(*#*(**(**(**(**(*-*(**(**(**(**(**(*{*(**(*s��Z$classnameX$classes]NSMutableData�]NSMutableDataVNSDataXNSObject� !"#$%&'()*_accumulatedDataSize_objectIdentifierWallURLs_identifierToDataDictionary_cacheDirectoryURL �
�����,-./0WNS.base[NS.relative� ��_�file:///private/var/mobile/Containers/Data/Application/42F0B6FF-EF3F-401B-AD02-0F7BA88F96FC/tmp/pasteboardDataPersister/506B8FA6-1808-4F66-A47C-1FDD133FC034�34UNSURL�3�678ZNS.objects��	�:;^NSMutableArray�:<WNSArray_$C7880DA1-AAA3-4B5C-9410-1F3518544264�?6@ABWNS.keys����DE_NSMutableDictionary�DF\NSDictionary�HI_ICDataPersister�J_ICDataPersister�LM_ICNotePasteboardData�N_ICNotePasteboardData    $ ) 2 7 I L Q S e k r � � � � � � � �������� 3FNk������������KPVY^ijlq��������������	#:=             O              T