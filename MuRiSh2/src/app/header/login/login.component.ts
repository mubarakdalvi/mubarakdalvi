import { Component } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ReactiveFormsModule], // have to import this for using formGroup in html file or it wil give error
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
})
export class LoginComponent {
  email = new FormControl('', [Validators.required, Validators.email]); //email validator
  password = new FormControl('', [
    // password validator with regex
    Validators.required, // validator required or will get error
    Validators.minLength(15), //max character 15
  ]);

  loginForm = new FormGroup({
    // group here with this form group and ReactiveFormsModule this is import module for using this in html as property
    email: this.email,
    password: this.password,
  });

  login() {
    this.loginForm.value;
    console.log(this.loginForm.value);
  }
  reset(){
    this.loginForm.reset;
    console.log(this.loginForm.reset);
  }
}
