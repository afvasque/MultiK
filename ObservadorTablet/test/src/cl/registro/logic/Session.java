package cl.registro.logic;

import java.util.ArrayList;

import java.util.List;

public class Session {
	
	public final static String FECHA_HORA_INICIO="horainicio";
	public final static String FECHA_HORA_FIN="horatermino";
	
	public Session(){
		listaAcciones=new ArrayList<Accion>();
	}
	private String fechaHoraInicio;
	private String fechaHoraTermino;
	private List <Accion>listaAcciones;
	public String getFechaHoraInicio() {
		return fechaHoraInicio;
	}
	public void setFechaHoraInicio(String fechaHoraInicio) {
		this.fechaHoraInicio = fechaHoraInicio;
	}
	public String getFechaHoraTermino() {
		return fechaHoraTermino;
	}
	public void setFechaHoraTermino(String fechaHoraTermino) {
		this.fechaHoraTermino = fechaHoraTermino;
	}
	public List<Accion> getListaAcciones() {
		return listaAcciones;
	}
	public void setListaAcciones(List<Accion> listaAcciones) {
		this.listaAcciones = listaAcciones;
	}
	
	

}
