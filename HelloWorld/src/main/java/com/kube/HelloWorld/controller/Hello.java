package com.kube.HelloWorld.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Hello {

    @GetMapping("/demo")
    public String greetings(){
        return "Hello World";
    }


}
