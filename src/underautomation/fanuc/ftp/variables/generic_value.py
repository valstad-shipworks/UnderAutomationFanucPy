import typing
from underautomation.fanuc.ftp.variables.value_kind import ValueKind
# Circular dependencies  : GenericField
from underautomation.fanuc.ftp.variables.generic_field import GenericField
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import GenericValue as generic_value

class GenericValue:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = generic_value()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def parent(self) -> 'GenericValue':
		return GenericValue(self._instance.Parent)
	@property
	def kind(self) -> ValueKind:
		return ValueKind(self._instance.Kind)
	@property
	def fields(self) -> typing.List[GenericField]:
		return [GenericField(x) for x in self._instance.Fields]
	@property
	def name(self) -> str:
		return self._instance.Name
	@property
	def is_uninitialized(self) -> bool:
		return self._instance.IsUninitialized
	@property
	def value(self) -> str:
		return self._instance.Value
	@property
	def register_name(self) -> str:
		return self._instance.RegisterName
	@property
	def full_name(self) -> str:
		return self._instance.FullName
