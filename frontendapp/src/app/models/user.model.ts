export interface User {
    user_name?: string;
    password: string; // Required for signup and signin
    join_date?: string; // Date in "YYYY-MM-DD" format
    membership?: string; // Defaults to 'regular' if not provided
    contact_number?: number;
    email_id: string;
    user_type?: string; // Defaults to 'customer' if not provided
  }