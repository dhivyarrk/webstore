import { Component } from '@angular/core';
import {User} from '../models/user.model';
import { AuthenticationService } from '../authentication.service';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';


@Component({
  selector: 'app-signup',
  imports: [FormsModule],
  templateUrl: './signup.component.html',
  styleUrl: './signup.component.scss'
})
export class SignupComponent {

  user: User = {
    user_name: '',
    password: '', // New password field
    membership: 'regular', // Default value
    contact_number: undefined,
    email_id: '',
    user_type: 'customer', // Default value
  }
    constructor(private authenticationService: AuthenticationService, private router: Router) {}

    onSubmit() {
      this.authenticationService.signup(this.user).subscribe({
        next: (response) => {
          alert('Signup successful!');
          console.log("signup");
          console.log(response);
          localStorage.setItem('token', response.user.token); // Save JWT token
          localStorage.setItem('user_type', response.user.user_type); // Save JWT token
          this.router.navigate(['/dashboard']); // Navigate to products page

        },
        error: (error) => alert('Error during signup: ' + error.message),
      });
    }
}
