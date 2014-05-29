package cl.registro.util;




import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.Result;
import javax.xml.transform.Source;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.xml.sax.InputSource;

import android.content.Context;
import android.util.Log;
import cl.registro.logic.Accion;
import cl.registro.logic.Session;


public class Persistencia {
	
	public static void escribeInformacionSesion(Session session,String filePath){
	
		File file = new File(filePath);
		file.setReadable(true);
		
		try {
			FileOutputStream fileOutputStream=new FileOutputStream(file);
			StringBuffer stringBuffer=new StringBuffer();
			stringBuffer.append("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
			stringBuffer.append("<session horainicio=\""+session.getFechaHoraInicio()+"\"  horatermino=\""+session.getFechaHoraTermino()+"\">");

			stringBuffer.append("<acciones>");
			for(Accion accion:session.getListaAcciones()){
				stringBuffer.append("<accion fecha=\""+accion.getFechaHora()+"\">\""+accion.getAccion()+"\"</accion>");			 
			}
			stringBuffer.append("</acciones>");
			stringBuffer.append("</session>");				
			
			fileOutputStream.write(stringBuffer.toString().getBytes());
			fileOutputStream.flush();
			fileOutputStream.close();
			
		} catch (Exception e) {
			Log.getStackTraceString(e);
		}
		

 }

	public  String getElementValue( Node elem ) {
        Node child;
     
        if( elem != null){
            if (elem.hasChildNodes()){
                for( child = elem.getFirstChild(); child != null; child = child.getNextSibling() ){
                    if( child.getNodeType() == Node.TEXT_NODE  ){
                        return child.getNodeValue();
                    }
                }
            }
        }
        return "";
    }

}
