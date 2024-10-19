package com.springboot.webapp.webapp.security;

import java.util.function.Function;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.security.web.SecurityFilterChain;
import static org.springframework.security.config.Customizer.withDefaults;

@Configuration
public class SecurityConfig {
	
	@Bean
	public InMemoryUserDetailsManager createIUser() {
		
		
		UserDetails user1 = createnewUser("eq", "password");
		UserDetails user2 = createnewUser("eq2", "password2");
		
		return new InMemoryUserDetailsManager(user1, user2);
	}

	private UserDetails createnewUser(String username, String password) {
		Function<String, String> passwordEncoder = input -> EncodePassword().encode(input);

		UserDetails user = User.builder()
							.passwordEncoder(passwordEncoder)
							.username(username)
							.password(password)
							.roles("USER", "ADMIN")
							.build();
		return user;
	}
	
	@Bean
	public PasswordEncoder EncodePassword() {
		return new BCryptPasswordEncoder();
	}
	
	@Bean
	public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
		http.authorizeHttpRequests(
				auth ->auth.anyRequest().authenticated());
		http.formLogin(withDefaults());
		
		http.csrf().disable();
		http.headers().frameOptions().disable();
		
		return http.build();
	}

}
