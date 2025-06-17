---
title: Qgis - Tasks
description: "Doing the heavy work in the background"
tags: programming, QGis
use: Transcript
languages: Python
dependences: QGis
---

> [!NOTE]
> The notes found here were creaded during studies of the PyQGIS developer cookbooks and [Using Threads in PyQGIS3 by Marco Bernasocchi](https://www.opengis.ch/2018/06/22/threads-in-pyqgis3/), so may snippets or texts may look similar (I wont reinvent the weel).

> necessary importtings
> ```python
> from qgis.core import (
> 	QgsProcessingContext,
> 	QgsTaskmanager,
> 	QgsTask,
> 	QgsProcessingAlgRunnerTask,
> 	Qgis,
> 	QgsProcessingFeedback,
> 	QgsApplication,
> 	QgsMessageLog,
> )
> ```

A task (`QgsTask`) is a container for the code to be performed in the backgorund, they can be grouped using *subtasks*. The control of the running tasks is made usually by the Task Manager (`QgsTaskManager`), but it can be done in a higher instance by the Global Task Manager (`QgsApplication.taskManager()`).

## Creating Tasks

There's three ways to **create new tasks**:

- Extending the `QgsTask` class:
	```python
	class NewUserTask(QgsTask):
		# do something
		pass
	```
- Creating one from a function `fromFunction(function, *args, on_finished=None, flags=2, **kwargs)`:
	```python
	def heavyFunction():
		# Some CPU intensive processing ...
		pass
	
	def workdone():
		# ... do something useful with the results
		pass

	task = QgsTask.fromFunction('heavy function', heavyFunction,on_finished=workdone)
	```

- Creating from a processing algo:
	```python
	params = dict()
	context = QgsProcessingContext()
	feedback = QgsProcessingFeedback()

	buffer_alg = QgsApplication.instance().processingRegistry().algorithmById('native:buffer')
	task = QgsProcessingAlgRunnerTask(buffer_alg, params, context,feedback)
	```

> [!WARNING]
> Any background task (regardless of how it is created) must NEVER use any QObject that lives on the main thread, such as accessing QgsVectorLayer, QgsProject or perform any GUI based operations like creating new widgets or interacting with existing widgets. Qt widgets must only be accessed or modified from the main thread. Data that is used in a task must be copied before the task is started. Attempting to use them from background threads will result in crashes.


> QUESTION: If the function is running inside of a custom processing script it "natively" avoid using the main thread of the application and alance the other ones, but there're some scripts that I've made that the load distribution between the threads are not equal, using a task will resolve the issue?

## Dependencies and subtasks

When a dependency is stated, the task manager will *automatically determine* how these dependencies will be executed. Wherever possible dependencies will be executed in parallel in order to satisfy them as quickly as possible. If a task on which another task depends is canceled, the dependent task will also be canceled. **Circular dependencies can make deadlocks possible, so be careful**.

Creating dependencies between tasks can be done using the [`addSubTask(self, subTask: QgsTask, dependencies: object = QgsTaskList(), subTaskDependency: QgsTask.SubTaskDependency = QgsTask.SubTaskIndependent)`](https://qgis.org/pyqgis/3.28/core/QgsTask.html#qgis.core.QgsTask.addSubTask) function.

If a task depends on a layer being available, this can be stated using the [`setDependentLayers(self, dependentLayers: Iterable[QgsMapLayer])`](https://qgis.org/pyqgis/3.28/core/QgsTask.html#qgis.core.QgsTask.setDependentLayers) function, if the layer isn't available, the task will be canceled.

## Running a Task

Once the task has been created (defined, or have its dependencies configured) it can be scheduled for running using the [`addTask(self, task: QgsTask, priority: int = 0)→ int`](https://qgis.org/pyqgis/3.28/core/QgsTaskManager.html#qgis.core.QgsTaskManager.addTask) function of the task manager.

**Adding a task to the manager automatically transfers ownership of that task to the manager**, and the manager will cleanup and delete tasks after they have executed. The scheduling of the tasks is influenced by the task priority, which is set in `addTask()`.

The status of tasks can be monitored using QgsTask and QgsTaskManager signals and functions.
