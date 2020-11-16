
public class ConsoleRegister implements Register{
	
	@Override
	public void getRegister(String message) {
		System.out.println(">> Console Register!!");
		System.out.println("Mensaje: " + message);
		
	}

}
