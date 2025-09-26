import typing
from underautomation.fanuc.ftp.list.errall_section_item import ErrallSectionItem
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.List import ErrorList as error_list

class ErrorList:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = error_list()
		else:
			self._instance = _internal
	@property
	def name(self) -> str:
		return self._instance.Name
	@property
	def items(self) -> typing.List[ErrallSectionItem]:
		return [ErrallSectionItem(x) for x in self._instance.Items]
