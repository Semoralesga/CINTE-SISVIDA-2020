import java.io.InputStream;
import java.util.Properties;

public class ConfigLoader { // Clase tomada de https://www.oscarblancarteblog.com/2014/07/18/patron-de-diseno-factory/

    private static Properties props;

    static {
        try {
            InputStream stream = ClassLoader.getSystemResourceAsStream("config/register.properties");
            ConfigLoader.props = new Properties();
            props.load(stream);
        } catch (Exception e) {
            throw new RuntimeException("Faild to load configuration");
        }
    }
    
    public static String getRegisterType(){
        return props.getProperty("registertype");
    }
    
    public static String getPropery(String propName){
        return props.getProperty(propName);
    }
    
    
}