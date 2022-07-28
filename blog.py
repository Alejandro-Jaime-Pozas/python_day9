# from IPython.display import clear_output

# Create a live blog with user in it, posts in it, the current user using it..

class Blog:
    
    def __init__(self):
        self.users = set()
        self.posts = []
        self.current_user = None
        
    # method to add new users to the blog
    def create_new_user(self):
        # get user info from input
        username = input("Please enter a username: ")
        # check is there is already a user w SAME USERNAME. ###############DID NOT UNDERSTAND FOR LOOP
        if username in {u.username for u in self.users}: # this is a set to check non-repeating values
            print(f"User with username {username} already exists")
        else:
            password = input("Please enter a password: ")
            # create a new user instance w info from input
            new_user = User(username, password)
            # add user instance to the list of blog users
            self.users.add(new_user)
            print(f"{new_user} has been created!")
            
    def log_user_in(self):
        # get user credentials
        username = input("What is your username: ")
        password = input("What is your password: ")
        for user in self.users:
            # check if that user has the same username and password as the inputs
            # PASSWORD SHOULD BE STORED DIFFERENTLY IN A DATABASE, CREATE HASHING TO SAFE-GUARD IT
            if user.username == username and user.check_password(password):
                # if user has correct credentials, set the blog's current user to that user instance
                self.current_user = user
                print(f"{user} has been logged in")
                break
        # if no users in our blog user list have correct username/password, let them know
        else:
            print("Username and/or password is incorrect")
            
    def log_user_out(self):
        # change the current_user attr from the user to None
        self.current_user = None
        print('You have successfully logged out')
       
    # method to create and add post to blog
    def create_post(self):
        # check to make sure the user trying to create a post is logged in
        if self.current_user is not None:
            # get title and body from the user input
            title = input("Enter the title of your post: ").title()
            body = input("Enter the body of your post: ")
            # create a new post instance w user input
            new_post = Post(title, body, self.current_user)
            # add the post object to the blog's list of posts
            self.posts.append(new_post)
            print(f"{new_post.title} has been created")
        else:
            print('You must be logged in to perform this action')
        
    # method to view all posts
    def view_posts(self):
        if self.posts:
            for post in self.posts:
                print(post)
        else:
            print('There are currently no posts for this blog :(')



class User:
    # class attribute to KEEP TRACK of User IDs
    id_counter = 1 
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.id = User.id_counter
        User.id_counter += 1

    def __str__(self):
        return self.username
    
    def __repr__(self):
        return f"<User {self.id}|{self.username}>"
    
    def check_password(self, password_guess):
        return self.password == password_guess



class Post:
    
    id_counter = 1
    
    def __init__(self, title, body, author):
        """
        title: str
        body: str
        author: user
        """
        self.title = title
        self.body = body
        self.author = author
        self.id = Post.id_counter
        Post.id_counter += 1
        
    def __str__(self):
        formatted_post = f"""
        {self.id} - {self.title.title()}
        By: {self.author}
        {self.body}
        """
        return formatted_post
    
    def __repr__(self):
        return f"<Post {self.id}|{self.title}>"
        

# Define fn to run blog

def run_blog():
#     Create an instance of the blog
    my_blog = Blog()
#     Keep looping while blog is 'running'
    while True:
#         be able to create new users
#         if there is no current user logged in
        if my_blog.current_user is None:
            print("1. Sign Up\n2. Log In\n3. View All Posts\n5. Quit")
            to_do = input("Which option would you like to choose: ")
            while to_do not in {'1', '5', '2', '3'}:
                to_do = input("Not valid. Please choose 1 or 5: ")
            # clear_output()
            if to_do == '5':
                print("Thanks for checking out our blog!")
                break
            elif to_do == '1':
                # method to create new user
                my_blog.create_new_user()
            elif to_do == '2':
                # method to log user in
                my_blog.log_user_in()
            elif to_do == '3':
                # method to view all posts
                my_blog.view_posts()
        # if there is a current user (aka a logged in user)
        else:
            print('1. Log Out\n2. Create a New Post\n3. View All Posts')
            to_do = input("Which option would you like to choose: ")
            while to_do not in {'1', '2', '3'}:
                to_do = input('Not valid. Please choose 1, 2, 3: ')
            # clear_output()
            if to_do == '1':
                my_blog.log_user_out()
            elif to_do == '2':
                my_blog.create_post()
            elif to_do == '3':
                my_blog.view_posts()
            





# Execute the fn
run_blog()