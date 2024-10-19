package com.springboot.webapp.webapp.login;

import java.util.ArrayList;
import java.util.List;

import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.SessionAttributes;

import com.springboot.webapp.webapp.task.Task;
import com.springboot.webapp.webapp.task.TaskRepo;

@Controller
@SessionAttributes("name")
public class LoginController {
	
	public LoginController(TaskRepo taskRepo) {
		super();
		this.taskRepo = taskRepo;
	}
	
	private TaskRepo taskRepo;
	
	@RequestMapping(value="/", method = RequestMethod.GET)
	public String login(ModelMap model) {
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
	
	private String getLoggedInUser() {
		Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
		return authentication.getName();
		
	}
	
}
