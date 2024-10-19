import os.path

from maa.resource import Resource
from maa.controller import AdbController
from maa.tasker import Tasker
from maa.toolkit import Toolkit


def main():
    user_path = os.path.join("tmp", "user")
    Toolkit.init_option(user_path)

    resource = Resource()
    resource.set_cpu()
    resource_path = os.path.join("assets", "resource")
    res_job = resource.post_path(resource_path)
    res_job.wait()

    adb_devices = Toolkit.find_adb_devices()
    if not adb_devices:
        print("No ADB device found.")
        exit()

    device = adb_devices[0]
    controller = AdbController(
        adb_path=device.adb_path,
        address=device.address,
        screencap_methods=device.screencap_methods,
        input_methods=device.input_methods,
        config=device.config,
    )
    controller.post_connection().wait()

    tasker = Tasker()
    tasker.bind(resource, controller)

    if not tasker.inited:
        print("Failed to init MAA.")
        exit()

    task_detail = tasker.post_pipeline("StopGame").wait().get()
    task_detail = tasker.post_pipeline("StartGame").wait().get()
    task_detail = tasker.post_pipeline("ClaimReward").wait().get()
    task_detail = tasker.post_pipeline("ChallengeLive").wait().get()


if __name__ == "__main__":
    main()
