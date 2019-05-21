import random
import unreal

all_actors = unreal.EditorLevelLibrary.get_all_level_actors()

unreal.log_warning("total actors: {}".format(len(all_actors)))

#for act in all_actors:
#	name = act.get_name()
#	rand = random.randint(1,100)
#	if(name.startswith("SM_ProductWithAN") and rand < 25):
#		unreal.log_warning("delete {}".format(name))
#		act.destroy_actor()

with unreal.ScopedSlowTask(len(all_actors), "Removing Products Randomly") as slow_task:
	slow_task.make_dialog(True)
	frame = 1
	for act in all_actors:
		if slow_task.should_cancel():
			break
		frame += 1
		slow_task.enter_progress_frame(frame)
		
		name = act.get_name()
		rand = random.randint(1,100)
		if(name.startswith("SM_ProductWithAN") and rand < 75):
			unreal.log_warning("delete {}".format(name))
			act.destroy_actor()