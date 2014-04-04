# -*- coding: utf-8 -*-
import logging

from spreads.plugin import PluginOption, HookPlugin, TriggerHooksMixin

class RPiPushButtonTrigger(HookPlugin, TriggerHooksMixin):
	""" Plugin for RPiPushButtonTrigger

	"""

	@classmethod
	def configuration_template(cls):
		""" Allows a plugin to define its configuration keys.

		The returned dictionary has to be flat (i.e. no nested dicts)
		and contain a PluginOption object for each key.

		Example::

		  {
		   'a_setting': PluginOption(value='default_value'),
		   'another_setting': PluginOption(value=[1, 2, 3],
										   docstring="A list of things"),
		   # In this case, 'full-fat' would be the default value
		   'milk': PluginOption(value=('full-fat', 'skim'),
								docstring="Type of milk",
								selectable=True),
		  }

		:return: dict with unicode: PluginOption(value, docstring, selection)
		"""
		return { 'pin_number': PluginOption(
				value=17, docstring="GPIO Pin to watch")}

	def __init__(self, config):
		self._logger = logging.getLogger('spreadsplug.RPiPushButtonTrigger')
		self._logger.debug("Initializing RPiPushButtonTrigger")
		self._trigger_pin = config['RPiPushButtonTrigger']['pin_number'].get(int)

	def start_trigger_loop(self, capture_callback):
		""" Start a thread that runs an event loop and periodically triggers
			a capture by calling the `capture_callback`.

		:param capture_callback:    The function to run for triggering a
									capture
		:type capture_callback:     function

		"""
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(buttonPin,GPIO.IN)

		self._exit_event = threading.Event()
		self._loop_thread = threading.Thread(target=self._trigger_loop,
				args=(capture_callback, ))
		self._logger.debug("Starting RPiPushButtonTrigger loop")
		self._loop_thread.start()

	def stop_trigger_loop(self):
		""" Stop the thread started by `start_trigger_loop*.

		"""
		if self._exit_event is None:
			# Return if no loop thread is running
			return
		self._logger.debug("Stopping RPiPushButtonTrigger loop")
		self._exit_event.set()
		self._loop_thread.join()

	def _trigger_loop(self, capture_func):
		# Polls all attached HID devices for a press->release event and
		# trigger a capture.
		while not self._exit_event.is_set():
			if (GPIO.input(self._trigger_pin)):
				capture_func()
