bplist00�
X$versionY$archiverT$topX$objects ��_NSKeyedArchiver�	Troot��+1259=>CGKU$null�_attributedStringData]dataPersisterV$class����WNS.dataO}�import sys
import usbmuxd
import time

def unlock_iphone(udid):
    client = usbmuxd.Client()
    iphone = None

    for i in range(10):
        try:
            iphone = client.get_device(udid)
            break
        except (usbmuxd.NoDeviceConnectedError, usbmuxd.DeviceNotFoundError) as e:
            time.sleep(1)

    if iphone is None:
        print("Failed to connect to iPhone.")
        return

    for i in range(100):
        try:
            iphone.send_message("lockdown", "do_set_passcode", {
                "passcodeEnabled": False
            })
            time.sleep(0.1)  # Adjust the sleep duration based on your testing
        except usbmuxd.MuxError as e:
            print(f"Failed to unlock the iPhone: {e}")
            break
        except (usbmuxd.NoDeviceConnectedError, usbmuxd.DeviceNotFoundError) as e:
            print(f"Device not found or connected: {e}")
            break

    client.release(iphone)

udid = "your-udid-here"
unlock_iphone(udid)*(**(*	*(**(**(*=*(**(**(*;*(*	*(*?*(*#*(**(*=*(**(**(**(*�*(**(*G*(*	*(*?*(*I*(*I��Z$classnameX$classes]NSMutableData�]NSMutableDataVNSDataXNSObject� !"#$%&'()*_accumulatedDataSize_objectIdentifierWallURLs_identifierToDataDictionary_cacheDirectoryURL �
�����,-./0WNS.base[NS.relative� ��_�file:///private/var/mobile/Containers/Data/Application/42F0B6FF-EF3F-401B-AD02-0F7BA88F96FC/tmp/pasteboardDataPersister/89ED5EEF-E0AC-462E-B2A5-C9E80A296A16�34UNSURL�3�678ZNS.objects��	�:;^NSMutableArray�:<WNSArray_$DCD62B96-6FE1-415D-B908-AF1933FAB440�?6@ABWNS.keys����DE_NSMutableDictionary�DF\NSDictionary�HI_ICDataPersister�J_ICDataPersister�LM_ICNotePasteboardData�N_ICNotePasteboardData    $ ) 2 7 I L Q S e k r � � � � � � � �249DM[_mt}������������������������� '/0138NR_dvy����             O              �