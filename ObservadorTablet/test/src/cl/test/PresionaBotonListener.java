package cl.test;

import java.io.FileOutputStream;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;

import cl.registro.logic.Accion;
import cl.registro.logic.Session;
import cl.registro.util.Persistencia;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;


public class PresionaBotonListener implements OnClickListener{
	
	private String filePath;
	private  Session session;
	private SimpleDateFormat simpleDateFormat;
	
	
	public SimpleDateFormat getSimpleDateFormat() {
		return simpleDateFormat;
	}



	public void setSimpleDateFormat(SimpleDateFormat simpleDateFormat) {
		this.simpleDateFormat = simpleDateFormat;
	}



	public Session getSession() {
		return session;
	}



	public void setSession(Session session) {
		this.session = session;
	}



	


	



	public String getFilePath() {
		return filePath;
	}



	public void setFilePath(String filePath) {
		this.filePath = filePath;
	}



	@Override
	public void onClick(View view) {
		Log.i("onClick",((Button)view).getText()+"");
		Accion accion=new Accion();
		
		accion.setFechaHora(simpleDateFormat.format(new Date()));
		int intId = ((Button)view).getId();
		switch(intId){
		// Habla sobre software
		case R.id.HSPH:
			accion.setAccion(""+"HSPH");
			break;
		case R.id.HSOH:
			accion.setAccion(""+"HSOH");
			break;
		case R.id.HSCH:
			accion.setAccion(""+"HSCH");
			break;
		case R.id.HSPM:
			accion.setAccion(""+"HSPM");
			break;
		case R.id.HSOM:
			accion.setAccion(""+"HSOM");
			break;
		case R.id.HSCM:
			accion.setAccion(""+"HSCM");
			break;
		//Habla sobre contenido
		case R.id.HCPH:
			accion.setAccion(""+"HCPH");
			break;
		case R.id.HCOH:
			accion.setAccion(""+"HCOH");
			break;
		case R.id.HCCH:
			accion.setAccion(""+"HCCH");
			break;
		case R.id.HCPM:
			accion.setAccion(""+"HCPM");
			break;
		case R.id.HCOM:
			accion.setAccion(""+"HCOM");
			break;
		case R.id.HCCM:
			accion.setAccion(""+"HCCM");
			break;
		//Habla sobre otra cosa
		case R.id.HOPH:
			accion.setAccion(""+"HOPH");
			break;
		case R.id.HOOH:
			accion.setAccion(""+"HOOH");
			break;
		case R.id.HOCH:
			accion.setAccion(""+"HOCH");
			break;
		case R.id.HOPM:
			accion.setAccion(""+"HOPM");
			break;
		case R.id.HOOM:
			accion.setAccion(""+"HOOM");
			break;
		case R.id.HOCM:
			accion.setAccion(""+"HOCM");
			break;
		//Molesta a 1 o varios compañeros
		case R.id.M1H:
			accion.setAccion(""+"M1H");
			break;
		case R.id.MVH:
			accion.setAccion(""+"MVH");
			break;
		case R.id.M1M:
			accion.setAccion(""+"M1M");
			break;
		case R.id.MVM:
			accion.setAccion(""+"MVM");
			break;
		// Distraccion sin disrupcion
		case R.id.DSDH:
			accion.setAccion(""+"DSDH");
			break;
		case R.id.DSDM:
			accion.setAccion(""+"DSDM");
			break;
		}

		session.getListaAcciones().add(accion);
		
	}

}
