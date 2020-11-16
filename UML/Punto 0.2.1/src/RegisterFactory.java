public class RegisterFactory {
    public static Register getRegister(){
        String registerType = ConfigLoader.getRegisterType();
        System.out.println("RegisterType => " + registerType);
        switch(registerType){
            case "Console":
                return new ConsoleRegister();
            case "File":
                return new FileRegister();
            //case "Database":
            //    return new DatabaseRegister();
            default:
                throw new RuntimeException("Unsupported register type");
        }
    }
}