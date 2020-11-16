
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
            Register Register = RegisterFactory.getRegister();
            Register.getRegister("Hola Mundo");
        } catch (Exception e) {
            e.printStackTrace();
        }

	}

}
