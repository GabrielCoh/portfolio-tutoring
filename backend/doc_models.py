from flask_restx import fields, Api

def initialize_models(api: Api):
    Login = api.model('Login', {
        'email': fields.String(required=True, description='User email', example="john@email.com"),
        'password': fields.String(required=True, description='User password', example="Johnd0e!")
    })
    
    UserId = api.model('UserId', {
        'id': fields.String(description="User id", example="07e1277b-77e7-47fa-9493-8d685ee2bba5"),
    })
    
    AdminId = api.model('AdminId', {
        'id': fields.String(description="Admin id", example="36c9050e-ddd3-4c3b-9731-9f487208bbc1"),
    })
    
    
    ProfessionId = api.model('ProfessionId', {
        'id': fields.String(description="Profession id", example="32491cac-9dfa-4c76-bcd6-499421c5c269"),
    })
    
    ReviewId = api.model('ReviewId', {
        'id': fields.String(description="Review id", example="82fe063d-fe6e-4b84-a12d-4400df168834"),
    })
    
    UserCreate = api.model('UserCreate', {
        'first_name': fields.String(required=True, description="User first name", example="John"),
        'last_name': fields.String(required=True, description="User last name", example="Doe"),
        'email': fields.String(required=True, description="User email", example="john@email.com"),
        'password': fields.String(required=True, description="User password", example="Johnd0e!")
    })
    
    AdminUserCreate = api.model('AdminUserCreate', {
        'first_name': fields.String(required=True, description="User first name", example="Peter"),
        'last_name': fields.String(required=True, description="User last name", example="Parker"),
        'email': fields.String(required=True, description="User email", example="peter@email.com"),
        'password': fields.String(required=True, description="User password", example="Sp1derman!"),
        'is_admin': fields.Boolean(description="role authorization", example=True)
    })
    
    ProfessionCreate = api.model('ProfessionCreate', {
        'title': fields.String(required=True, description='Title of the profession', example='Music teacher'),
        'description': fields.String(description='Description of the profession', example='Teaching music in highschool'),
        'price': fields.Float(required=True, description='Price per session', example=50.0)
    })
    
    ProfessionUpdate = api.model('ProfessionUpdate', {
        'title': fields.String(description='Title of the profession', example='Music and Arts teacher'),
        'description': fields.String(description='Description of the profession', example='Teaching Music and Arts in highschool'),
        'price': fields.Float(description='Price per session', example=70.0)
    })
    
    ReviewCreate = api.model('ReviewCreate', {
        'text': fields.String(required=True, description='Text of the review', example="Super cool!"),
        'rating': fields.Integer(required=True, description='Rating of the profession (1-5)', example=5),
        'profession_id': fields.String(required=True, description='ID of the profession', example="32491cac-9dfa-4c76-bcd6-499421c5c269")
    })
    
    ReviewUpdate = api.model('ReviewUpdate', {
        'text': fields.String(description='Text of the review', example="Not So Good"),
        'rating': fields.Integer(description='Rating of the place (1-5)', example=3),
    })
    
    LoginResponse = api.model('LoginResponse', {
        "access_token": fields.String(description='Token', example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MTk2MTQ5MCwianRpIjoiZjZlM2Y4ZTEtZmM4MC00ODY3LTliZDktNGQwZDJkZGJhZDBhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6IjYwZjU2MDhiLTE5N2QtNGFjNC05MGQ0LWVjZjM4NWFiYWVlMyIsImlzX2FkbWluIjpmYWxzZX0sIm5iZiI6MTc0MTk2MTQ5MCwiY3NyZiI6IjRiZjllZmU0LTJkODAtNDBlMC1iMjE5LTgzNDc3MzliY2EyNSIsImV4cCI6MTc0MTk2MjM5MH0.N3xtpc6Ha-3wmXTSbz94Z_A7hkuswgrHrD6h4_XUlxk")
    })
    
    UserResponse = api.inherit('UserResponse', UserId, {
        'first_name': fields.String(description="User first name", example="John"),
        'last_name': fields.String(description="User last name", example="Doe"),
        'email': fields.String(description="User email", example="john@email.com")
    })
    
    AdminUserCreateResponse = api.inherit('AdminUserCreateResponse', AdminId, {
        'first_name': fields.String(required=True, description="User first name", example="Peter"),
        'last_name': fields.String(required=True, description="User last name", example="Parker"),
        'email': fields.String(required=True, description="User email", example="peter@email.com"),
        'is_admin': fields.Boolean(description="role authorization", example=True)
    })
    
    AdminUserUpdateResponse = api.inherit('AdminUserUpdateResponse', AdminId, {
        'first_name': fields.String(description="User first name", example="Peter"),
        'last_name': fields.String(description="User last name", example="Parker"),
        'email': fields.String(description="User email", example="peter@spiderman.com"),
        'is_admin': fields.Boolean(description="role authorization", example=False)
    })
    
    
    ProfessionResponse = api.inherit('ProfessionResponse', ProfessionId, {
        'title': fields.String(description='Title of the profession', example='Instructive lesson'),
        'description': fields.String(description='Description of the profession', example='A nice teacher to have'),
        'price': fields.Float(description='Price per session', example=50.0),
  })
    
    ReviewResponse = api.inherit('ReviewResponse', ReviewId, {
        'rating': fields.Integer(description="Rating", example=5),
        'text': fields.String(description="Text", example="Super cool!"),
        'profession_id': fields.String(description="Profession id", example="a6e9d55e-c8d1-4268-bb65-4c19a5206a08"),
        'user_id': fields.String(description="User id", example="c28c8c27-b900-409b-ab4d-cc215cb2f518")
    })
    
    InvalidCredentials = api.model('InvalidCredentials', {
        'message': fields.String(description="Error msg", example="Invalid credentials")
    })
    
    InvalidInput = api.model('InvalidInput', {
        'message': fields.String(description="Error msg", example="<error_message>")
    })
    
    NotFound = api.model('NotFound', {
        'message': fields.String(description="Error msg", example="<entity> not found")
    })
    
    UnauthorizedAction = api.model('UnauthorizedAction', {
        'message': fields.String(description="Error msg", example="Unauthorized action")
    })
    
    AdminPrivileges = api.model('AdminPrivileges', {
        'message': fields.String(description="Error msg", example="Admin privileges required")
    })
    
    Updated = api.model('Updated', {
        'message': fields.String(description="Update success", example="<entity> updated successfully")
    })
    
    Deleted = api.model('Deleted', {
        'message': fields.String(description="Delete success", example="<entity> deleted successfully")
    })
    
    UsersList = api.model('UsersList', {
        'Users': fields.List(fields.Nested(UserResponse))
    })
    
      ProfessionsList = api.model('ProfessionsList', {
        'Professions': fields.List(fields.Nested(ProfessionResponse))
    })
    
    ReviewsList = api.model('ReviewsList', {
        'Reviews': fields.List(fields.Nested(ReviewResponse))
    })
    
    UserUpdate = api.model('UserUpdate', {
        'first_name': fields.String(description='First name of the user', example="Jane"),
        'last_name': fields.String(description='Last name of the user', example="Doe"),
    })
    
    UserUpdateResponse = api.inherit('UserUpdateResponse', UserId, {
        'first_name': fields.String(description='First name of the user', example="Jane"),
        'last_name': fields.String(description='Last name of the user', example="Doe"),
        'email': fields.String(description="User email", example="john@email.com")
    })
    
    AdminUserUpdate = api.model('AdminUserUpdate', {
        'first_name': fields.String(description="User first name", example="Peter"),
        'last_name': fields.String(description="User last name", example="Parker"),
        'email': fields.String(description="User email", example="peter@spiderman.com"),
        'password': fields.String(description="User password", example="Sp1derman!"),
        'is_admin': fields.Boolean(description="role authorization", example=False)
    })
    
    ProfessionByIdResponse = api.model('ProfessionByIdResponse', {
        'id': fields.String(description="Place id", example="a6e9d55e-c8d1-4268-bb65-4c19a5206a08"),
        'title': fields.String(description='Title of the profession', example='Instructive lesson'),
        'description': fields.String(description='Description of the profession', example='A nice teacher to have'),
        'price': fields.Float(description='Price per session', example=50.0),
        'owner': fields.Nested(UserResponse),
        'reviews': fields.List(fields.Nested(ReviewResponse), description='List of detailed reviews'),
    })
    
    ReviewsProfessionList = api.model('ReviewsProfessionList', {
        'ReviewsProfession': fields.List(fields.Raw, example=[
            {
                'id': "82fe063d-fe6e-4b84-a12d-4400df168834",
                'rating': 5,
                'text': "Super cool!",
            }
        ])
    })
    
    return {
        # CommonRes
        "InvalidInput": InvalidInput,
        "NotFound": NotFound,
        "UnauthorizedAction": UnauthorizedAction,
        "InvalidCredentials": InvalidCredentials,
        "AdminPrivileges": AdminPrivileges,
        "Updated": Updated,
        "Deleted": Deleted,
        # User
        "UserCreate": UserCreate,
        "UserResponse": UserResponse,
        "UsersList": UsersList['Users'],
        "UserUpdate": UserUpdate,
        "UserUpdateResponse": UserUpdateResponse,
        # Login
        "Login": Login,
        "LoginResponse": LoginResponse,
        # Profession
        "ProfessionCreate": ProfessionCreate,
        "ProfessionUpdate": ProfessionUpdate,
        "ProfessionResponse": ProfessionResponse,
        "ProfessionsList": ProfessionsList['Professions'],
        "ProfessionByIdResponse": ProfessionByIdResponse,
        "ReviewsProfessionList": ReviewsProfessionList['ReviewsProfession'],
        # Review
        "ReviewCreate": ReviewCreate,
        "ReviewResponse": ReviewResponse,
        "ReviewsList": ReviewsList['Reviews'],
        "ReviewUpdate": ReviewUpdate,
        # Admin
        "AdminUserCreate": AdminUserCreate,
        "AdminUserCreateResponse": AdminUserCreateResponse,
        "AdminUserUpdate": AdminUserUpdate,
        "AdminUserUpdateResponse": AdminUserUpdateResponse,
        "AmenityCreate": AmenityCreate,
        "AmenityResponse": AmenityResponse,
        "AmenityUpdate": AmenityUpdate,
        
    }

