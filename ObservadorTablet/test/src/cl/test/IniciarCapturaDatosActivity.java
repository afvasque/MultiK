package cl.test;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.Menu;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ArrayAdapter;
import android.widget.Spinner;

public class IniciarCapturaDatosActivity extends Activity implements OnClickListener {
	public static final String FILE_NAME="NOMBRE_ARCHIVO";
	private Spinner spinner0, spinner1;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_iniciar_captura_datos);
		
		findViewById(R.id.iniciar_captura).setOnClickListener(this);
		       
       
	    spinner0 = (Spinner) findViewById(R.id.spinner0);
	    Spinner spinner0 = (Spinner) findViewById(R.id.spinner0);
        ArrayAdapter<CharSequence> adapter0 = ArrayAdapter.createFromResource(
                this, R.array.colegio_array, android.R.layout.simple_spinner_item);
        		adapter0.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner0.setAdapter(adapter0);
        
        spinner1 = (Spinner) findViewById(R.id.spinner1);
        Spinner spinner1 = (Spinner) findViewById(R.id.spinner1);
        ArrayAdapter<CharSequence> adapter1 = ArrayAdapter.createFromResource(
                this, R.array.cursos_array, android.R.layout.simple_spinner_item);
        		adapter1.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner1.setAdapter(adapter1);
        
    }

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		
		getMenuInflater().inflate(R.menu.iniciar_captura_datos, menu);
		return true;
	}

	@Override
	public void onClick(View v) {
		
		String nombreArchivo=null;
		
		nombreArchivo="data."+String.valueOf(spinner0.getSelectedItem())+".Curso"+String.valueOf(spinner1.getSelectedItem())+"."+System.currentTimeMillis();
		
		if(nombreArchivo!=null && !"".equals(nombreArchivo)){
			 Intent intent = new Intent(this, RegistraDatosActivity.class);
			   intent.putExtra(FILE_NAME, nombreArchivo);
			    startActivity(intent);
		}
	}
}
