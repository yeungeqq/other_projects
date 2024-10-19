package com.springboot.webapp.webapp.task;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.SessionAttributes;

import jakarta.validation.Valid;

@Controller
@SessionAttributes("name")
public class TaskControllerJpa {
		
	public TaskControllerJpa(TaskRepo taskRepo) {
		super();
		this.taskRepo = taskRepo;
	}
	
	private TaskRepo taskRepo;

	@RequestMapping("tasks")
	public String taskList(ModelMap model) {
		model.put("name", getLoggedInUser());
		String username = getLoggedInUser();
		List<Task> tasks = taskRepo.findByUsername(username);
		List<Task> openTasks = new ArrayList<>();
		for (Task task: tasks) {
			if (task.getComplete().equals("No")) openTasks.add(task);
		}
		model.addAttribute("tasks", openTasks);
		
		return "tasks";
	}
	
	@RequestMapping("complete-tasks")
	public String completeTaskList(ModelMap model) {
		model.put("name", getLoggedInUser());
		String username = getLoggedInUser();
		List<Task> tasks = taskRepo.findByUsername(username);
		List<Task> completeTasks = new ArrayList<>();
		for (Task task: tasks) {
			if (task.getComplete().equals("Yes")) completeTasks.add(task);
		}
		model.addAttribute("tasks", completeTasks);
		
		return "completetasks";
	}

	private String getLoggedInUser() {
		Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
		return authentication.getName();
	}

	@RequestMapping(value="add-task", method=RequestMethod.GET)
	public String showAddTaskPage(ModelMap model) {
		String username = getLoggedInUser();
		Task task = new Task(0, username, "", LocalDate.now(), "No");
		model.put("task", task);
		return "addtask";
	}
	
	@RequestMapping(value="add-task", method=RequestMethod.POST)
	public String addTask(ModelMap model, @Valid Task task, BindingResult result) {
		
		if(result.hasErrors()) return "addtask";			
		
		String username = getLoggedInUser();
		task.setUsername(username);
		taskRepo.save(task);
		return "redirect:tasks";
	}
	
	@RequestMapping("delete-task")
	public String deleteTask(@RequestParam int id) {
		taskRepo.deleteById(id);
		return "redirect:tasks";
	}
	
	@RequestMapping("delete-complete-task")
	public String deleteCompleteTask(@RequestParam int id, ModelMap model) {
		taskRepo.deleteById(id);
		model.put("name", getLoggedInUser());
		String username = getLoggedInUser();
		List<Task> tasks = taskRepo.findByUsername(username);
		List<Task> completeTasks = new ArrayList<>();
		for (Task task: tasks) {
			if (task.getComplete().equals("Yes")) completeTasks.add(task);
		}
		model.addAttribute("tasks", completeTasks);
		
		return "completetasks";
	}
	
	@RequestMapping("update-complete-task")
	public String updateCompleteTask(@RequestParam int id) {
		Task task = taskRepo.findById(id).get();
		task.setComplete("Yes");
		taskRepo.save(task);
		return "redirect:tasks";
	}
	
	@RequestMapping(value="update-task", method = RequestMethod.GET)
	public String showUpdateTaskPage(@RequestParam int id, ModelMap model) {
		Task task = taskRepo.findById(id).get();
		model.addAttribute("task", task);
		return "addtask";
	}
	
	@RequestMapping(value="update-task", method=RequestMethod.POST)
	public String updateTask(ModelMap model, @Valid Task task, BindingResult result) {
		
		if(result.hasErrors()) return "addtask";			
		
		String username = getLoggedInUser();
		task.setUsername(username);
		taskRepo.save(task);
		return "redirect:tasks";
	}
}
