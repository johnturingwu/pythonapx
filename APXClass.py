import sys,os
import clr
clr.AddReference("ANST.API")
from AudioPrecision.API import *
from System.IO import Directory, Path


class APX:
    # def __init__(self,):
    #     mode = APxOperatingMode.SequenceMode
    def init_apx(self, mode=APxOperatingMode.SequenceMode):
        APx = APx500(mode, True)
        APx.Visible = True
        return APx

    def open_project(self,filepath):
        directory = Directory.GetCurrentDirectory()
        fullpath = os.path.join(directory, filepath)
        if not os.path.exists(fullpath):
            fullpath = filepath
        APx = self.init_apx()
        APx.OpenProject(fullpath)
        return APx

    def add_siginal_path(self):
        class_apx = self.init_apx().AddSignalPath()
        return class_apx

    def add_measurement(self, signal_name="Signal Path1", measure_name="POLQA"):
        class_apx = self.init_apx().AddMeasurement(signal_name, measure_name)
        return class_apx

    def add_result(self, signal_path_index, insert_position, result_type):
        self.init_apx().AddResult(signal_path_index, insert_position, result_type)

    def cancel_operation(self):
        self.init_apx().CancelOperation()

    def clear_last_exception(self):
        self.init_apx().ClearLastException()

    def copy_measurement_clipboard(self, signal_path, measurement):
        self.init_apx().CopyMeasurementToClipboard(signal_path, measurement)

    def copy_signal_path_clipboard(self, sign_path):
        self.init_apx().CopySignalPathToClipboard(sign_path)

    def show_measurement(self, signal_name="Signal Path1", measure_name="POLQA"):
        class_apx = self.init_apx().ShowMeasurement(signal_name, measure_name)
        return class_apx

    def get_squence_info(self, signal_name="Signal Path1", measure_name="POLQA"):
        class_apx = self.init_apx().Sequence[signal_name][measure_name]
        return class_apx

    def run_measurement(self, class_apx):
        class_apx.Run()

    def delete_result(self, signal_path_index, measurement_index, result_index):
        self.init_apx().DeleteResult(signal_path_index, measurement_index, result_index)

    def delete_signal_path(self, index_or_name):
        self.init_apx().DeleteSignalPath(index_or_name)

    def max(self):
        return self.init_apx().Maximize()

    def min(self):
        return self.init_apx().Minimize()

    def paste_from_clipboard(self):
        self.init_apx().PasteFromClipboard()

    def save_project(self, file_path, Apx):
        Apx.SaveProject(file_path)

    def exit(self):
        self.init_apx().Exit()




# a = APX()
# a.add_measurement("Signal Path5", "POLQA")


